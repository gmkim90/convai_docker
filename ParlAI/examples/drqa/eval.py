# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
"""Script to run evaluation only on a pretrained model."""
try:
    import torch
except ModuleNotFoundError:
    raise ModuleNotFoundError('Need to install pytorch: go to pytorch.org')
import logging

import pdb

from parlai.agents.drqa.utils import Timer
from parlai.agents.drqa.agents import DocReaderAgent
from parlai.core.params import ParlaiParser
from parlai.core.worlds import create_task


def main(opt):
    # Check options
    assert('pretrained_model' in opt)
    assert(opt['datatype'] in {'test', 'valid'})

    # Calculate TDNN embedding dim (after applying TDNN to char tensor)
    opt['kernels'] = ''.join(opt['kernels'])
    if isinstance(opt['kernels'], str):
        opt['kernels'] = eval(opt['kernels']) # convert string list of tuple --> list of tuple

    if opt['add_char2word']:
        opt['NULLWORD_Idx_in_char'] = opt['vocab_size_char']-1
        opt['embedding_dim_TDNN']=0
        for i, n in enumerate(opt['kernels']):
            opt['embedding_dim_TDNN'] += n[1]

        logger.info('TDNN embedding dim = %d' % (opt['embedding_dim_TDNN']))

    #Write prediction file
    f_predict = open((str(opt['model_file']) + '.prediction'),"w")
    f_predict.write("{")
    f_analysis = open((str(opt['model_file']) + '.analysis'),"w")

    # Load document reader
    doc_reader = DocReaderAgent(opt)

    # Log params
    logger.info('[ Created with options: ] %s' % ''.join(['\n{}\t{}'.format(k, v) for k, v in doc_reader.opt.items()]))

    logger.info('[ Running validation... ]')
    valid_world = create_task(opt, doc_reader)
    valid_time = Timer()

    # Sent prediction
    #pdb.set_trace()
    valid_world.agents[1].opt['ans_sent_predict'] = False
    valid_world.agents[1].model.network.opt['ans_sent_predict'] = False  # disable sentence predicction by default
    if opt['ans_sent_predict']:
        valid_world.agents[1].model.input_idx_bdy -= 1

    nExample = 0
    f1_avg_prev = 0
    acc_avg_prev = 0
    for _ in valid_world:
        pdb.set_trace()
        valid_world.parley()
        nExample+=1
        #pdb.set_trace()
        f_predict.write('"' + valid_world.acts[0]['reward'] + '" ')
        f_predict.write('"' + valid_world.acts[1]['text'] + '", ')

        f_analysis.write('Paragraph & Question = ' + valid_world.acts[0]['text'] + '\n')
        f_analysis.write('Prediction = ' + valid_world.acts[1]['text'] + '\n')
        f_analysis.write('Answer = ' + valid_world.agents[0].lastY_prev[0] + '\n')

        f1_avg_cur = valid_world.agents[0].report()['f1']
        f1_cur = nExample*f1_avg_cur - (nExample-1)*f1_avg_prev
        f_analysis.write('F1 = ' + str(f1_cur) + '\n')
        f1_avg_prev = f1_avg_cur

    #pdb.set_trace()
    metrics = valid_world.report()
    if 'tasks' in metrics:
        for task, t_metrics in metrics['tasks'].items():
            logger.info('task = %s | EM = %.4f | F1 = %.4f | exs = %d | ' %(task, t_metrics['accuracy'], t_metrics['f1'], t_metrics['total']))
        logger.info('Overall EM = %.4f | exs = %d' % (metrics['accuracy'], metrics['total']))
    else:
        logger.info('EM = %.4f | F1 = %.4f | exs = %d' % (metrics['accuracy'], metrics['f1'], metrics['total']))
    logger.info('[ Done. Time = %.2f (s) ]' % valid_time.time())

    # Close prediction file
    f_predict.write("}")
    f_predict.close()
    f_analysis.close()

if __name__ == '__main__':
    # Get command line arguments
    argparser = ParlaiParser()
    DocReaderAgent.add_cmdline_args(argparser)
    opt = argparser.parse_args()

    # Set logging (only stderr)
    logger = logging.getLogger('DrQA')
    logger.setLevel(logging.INFO)
    fmt = logging.Formatter('%(asctime)s: %(message)s', '%m/%d/%Y %I:%M:%S %p')
    console = logging.StreamHandler()
    console.setFormatter(fmt)
    logger.addHandler(console)

    # Set cuda
    opt['cuda'] = not opt['no_cuda'] and torch.cuda.is_available()
    if opt['cuda']:
        logger.info('[ Using CUDA (GPU %d) ]' % opt['gpu'])
        torch.cuda.set_device(opt['gpu'])

    # Run!
    main(opt)
