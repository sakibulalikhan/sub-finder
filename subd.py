import requests 
import sys 

print(r"""

   _____           _                    ______   _               _               
  / ____|         | |                  |  ____| (_)             | |              
 | (___    _   _  | |__      ______    | |__     _   _ __     __| |   ___   _ __ 
  \___ \  | | | | | '_ \    |______|   |  __|   | | | '_ \   / _` |  / _ \ | '__|
  ____) | | |_| | | |_) |              | |      | | | | | | | (_| | |  __/ | |   
 |_____/   \__,_| |_.__/               |_|      |_| |_| |_|  \__,_|  \___| |_|   
                                                                                 
                                                                                 

""")
print("\n****************************************************************")
print("\n* Copyright of Sakibul Ali Khan.                               *")
print("\n* Twitter: https://twitter.com/sakibulalikhan                  *")
print("\n* Linkedin: https://www.linkedin.com/in/sakibulalikhan/        *")
print("\n****************************************************************")
print("\n")

domain = input("Enter domain name: ")

sub_list = open("subdomains-10000.txt").read() 
subs = sub_list.splitlines()

for sub in subs:
    domian = f"http://{sub}.{domain}" 

    try:
        requests.get(domian)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("\nValid subdomain: ",domian)