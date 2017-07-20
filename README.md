# convai_docker


설치
1) clone this project
2) put glove in data/glove.840B.300d.txt
3) download model from slack and extract

실행법

1) python run-demo-simple.py  --> https server execution

2) CC mode example
python get_answer_cnsl.py --paragraph "dummy" --question "who are you ?"

3) QA mode example
python get_answer_cnsl.py --paragraph "sample paragraph ha ha ha" --question "what is the name of sample paragraph ?"
