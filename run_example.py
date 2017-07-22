import subprocess

if __name__ == '__main__':
    paragraph="sample paragraph"
    question="sample question"
    
    resp = subprocess.check_output(["python3", "get_answer_cnsl.py",
                                   "--paragraph", paragraph, "--question", question])

    resp = str(resp, "utf-8")   
    print('resp = ' + resp )
