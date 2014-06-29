import webbrowser
import sys
import time
import random

#flips = input("How Many Searches?\n")
words = open('/etc/dictionaries-common/words').readlines()
urlStem = "http://www.bing.com/search?q="
i = 0

while i < 31:
	webbrowser.open(urlStem + str(random.choice(words)))
	i += 1
	time.sleep(15)
