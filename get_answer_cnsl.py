import requests
import argparse
import pdb

parser = argparse.ArgumentParser(description='Get answer')
parser.add_argument('--paragraph', type=str, help='Paragraph', required=True)
parser.add_argument('--question', type=str, help='Question', required=True)

if __name__ == '__main__':
    args = parser.parse_args()
    #pdb.set_trace()
    resp = requests.get(
        'http://0.0.0.0:1990/submit',
        params={'question': args.question, 'paragraph': args.paragraph})

    print(resp.text)
