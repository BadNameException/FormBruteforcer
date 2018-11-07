# 32-126 : 20-7E
#
import subprocess

password = []
custom_ascii = [' ','!','\"','#','$','%','&','\'','(',')','*','+'',','-','.','/','0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','[','\\',']','^','_','`','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','{','|','}','~']

class ASCII:
    def __init__(self):
        print ("Skriver til ASCII")

    def build_pw(self):
        cracked = bool(False)
        while cracked:
            print "Hallo"



class BruteForce:

    def __init__(self):
        pass

    def start_thread(self, password):
        # Legg threadname/ID i en liste
        # Hent nytt passord
        # connect_ssh
        # slett fra liste
        # start ny tråd



    def connect_ssh(self, pword):

        output = subprocess.Popen(["./bf_script.sh hallo"], stdout=subprocess.PIPE, shell=True)
        (outp, error) = output.communicate()
        print "Output: ", outp
        print "Error: ", error

        proc = subprocess.Popen(["sshpass -p " + pword + " ssh -o StrictHostKeyChecking=no 10.225.147.156 -p 2222"], stdout=subprocess.PIPE, shell=True)
        (out, err) = proc.communicate()
        print "program output: ", out
        print "program error: ", err

        return


# min main

pw = "hallo"

bf = BruteForce()
bf.start_thread(pw)
custom_ascii = (" !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~")