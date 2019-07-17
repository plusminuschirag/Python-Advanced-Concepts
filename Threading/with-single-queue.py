from queue import Queue,Empty
from threading import Thread
import verifier
import json

THREAD_POOL_SIZE = 4

mails = ["chiragsharma1906@gmail.com","iamcshhhdhdhdhdh@gmail.com","chiragsharmagtbit@outlook.com","wahtergate@gmail.com","waterpark@outlook.com","lalallalalalala@gmail.com"]

def mailVerify(mailQueue):
    while not mailQueue.empty():
        try:
            mail = mailQueue.get(block=False)
        except Empty:
            break
        else:
            if verifier.verify(mail, '17d753c1aaa19cba5323599ff6d603eb8c6502e1677a6cee869d6a659a1b11f3'):
                print("Right")
            else:
                print("Wrong")
            mailQueue.task_done()

mailQueue = Queue()
for mail in mails:
    mailQueue.put(mail)

threads = [Thread(target=mailVerify,args=(mailQueue,)) for _ in range(THREAD_POOL_SIZE)]
print(threads)

for thread in threads:
    thread.start()

mailQueue.join()

while threads:
    threads.pop().join()