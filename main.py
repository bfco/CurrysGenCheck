from operator import contains
from unittest import skip
from attr import NOTHING
import requests
from bs4 import BeautifulSoup
import random
from datetime import datetime
import os

clear = lambda: os.system('cls')
clear()
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("[ INFO ] [ " + t + " ] Initializing Program...")
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("""\033[36m
   ██████╗██╗   ██╗██████╗ ██████╗ ██╗   ██╗███████╗
  ██╔════╝██║   ██║██╔══██╗██╔══██╗╚██╗ ██╔╝██╔════╝
  ██║     ██║   ██║██████╔╝██████╔╝ ╚████╔╝ ███████╗            \033[95m┏━━━━━━━━━━━━━━━━━━ Info ━━━━━━━━━━━━━━━━┓\033[36m
  ██║     ██║   ██║██╔══██╗██╔══██╗  ╚██╔╝  ╚════██║                \033[95m@\033[0m Version: 1.0\033[36m 
  ╚██████╗╚██████╔╝██║  ██║██║  ██║   ██║   ███████║		    \033[95m@\033[0m Time: """ + t + """\t\033[36m
   ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ 	            \033[95m@\033[0m Made with love \033[36m   
  ██╗     ██╗███╗   ██╗██╗  ██╗     ██████╗ ███████╗███╗   ██╗	    \033[95m@\033[0m Author: bfcoV4#2049\033[36m
  ██║     ██║████╗  ██║██║ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║	\033[95m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\033[36m	    
  ██║     ██║██╔██╗ ██║█████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║		
  ██║     ██║██║╚██╗██║██╔═██╗     ██║   ██║██╔══╝  ██║╚██╗██║	
  ███████╗██║██║ ╚████║██║  ██╗    ╚██████╔╝███████╗██║ ╚████║                                                
  ╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝     ╚═════╝ ╚══════╝╚═╝  ╚═══╝
                                                               
                                                          
       """)

input(("[ INPUT ] [ " + t + " ] Press ENTER key to start."))
while (True):
    def count_words(url, the_word):
        r = requests.get(url).text    
        return r.count(the_word)


    import string
    string = string.digits+string.ascii_letters
    url = "https://currys.co/"
    letters = ''.join(random.choice(string) for i in range(17))
    links = url + letters

    def main():
        url = links
        word = 'currys'
        count = count_words(url, word)
        if count != 8:
            now = datetime.now()
            t = now.strftime("%H:%M:%S")
            print("\033[31m[ SYSTEM ] [ " + t + " ] Dead Link")
        else: 
            now = datetime.now()
            t = now.strftime("%H:%M:%S")
            print("\033[92m\n[ SYSTEM ] [ " + t + " ] Url: {}\nIS A WINNING LINK!".format(url))
            input('Press any key to continue')

    if __name__ == '__main__':
        main()
