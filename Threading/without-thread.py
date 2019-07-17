import verifier
import json
import time

mails = ["chiragsharma1906@gmail.com","iamcshhhdhdhdhdh@gmail.com","chiragsharmagtbit@outlook.com"]
for mail in mails:
    if verifier.verify(mail, '17d753c1aaa19cba5323599ff6d603eb8c6502e1677a6cee869d6a659a1b11f3'):
        print("Right")
    else:
        print("Wrong")