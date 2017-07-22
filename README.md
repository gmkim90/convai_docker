# convai_docker

Install 

1) clone this project
2) download glove.840B.300d.txt (from http://nlp.stanford.edu/data/glove.840B.300d.zip) and put in data/glove.840B.300d.txt
3) download model.zip extract it
      
      A. source1 : 143.248.47.31:/data/kAIb/model.zip
     
      B. source2 : google drive link (will be sent soon)

4) install nvidia-docker ( https://github.com/NVIDIA/nvidia-docker)

How to run

1) sudo nvidia-docker run -w /app -p 1990:1990 -v {/path/to/convai_docker}:/app calee/kaib python run-demo-simple.py  --> https server execution

2) CC mode example
python get_answer_cnsl.py --paragraph "dummy" --question "how old are you ?"

3) QA mode example
python get_answer_cnsl.py --paragraph 'In the late 1980s, according to "Richard Feynman and the Connection Machine", Feynman played a crucial role in developing the first massively parallel computer, and in finding innovative uses for it in numerical computations, in building neural networks, as well as physical simulations using cellular automata (such as turbulent fluid flow), working with Stephen Wolfram at Caltech. His son Carl also played a role in the development of the original Connection Machine engineering; Feynman influencing the interconnects while his son worked on the software.' --question "Which article mention about Feynman's role developing parallel computer ?"
