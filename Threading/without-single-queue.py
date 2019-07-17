from threading import Thread
import verifier
import json

#Not a good idea to create infinite threads for infinite objects. Will impose heavy duty over the memory for no 
#good reason

mails = ["chiragsharma1906@gmail.com","iamcshhhdhdhdhdh@gmail.com","chiragsharmagtbit@outlook.com"]

def mailVerify(mail):
    if verifier.verify(mail, '17d753c1aaa19cba5323599ff6d603eb8c6502e1677a6cee869d6a659a1b11f3'):
        print("Right")
    else:
        print("Wrong")


threads = []
for mail in mails:
    thread = Thread(target=mailVerify,args=[mail])
    thread.start()
    threads.append(thread)

while threads:
    threads.pop().join()