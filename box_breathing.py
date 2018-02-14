import time
import sys


def print_no_newline(string):
    sys.stdout.write(string)
    sys.stdout.flush()

def breath(step):
    print_no_newline(step + " ")
    for i in range(1,6):
        time.sleep(1)
        print_no_newline(str(i) + " ")
    print " "

steps = ["Inhale", "Hold  ", "Exhale", "Hold  "]

for i in range(1,3):
    for i in steps:
        breath(i)
    print "----------------"
