# convai_docker


<<<<<<< HEAD
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

