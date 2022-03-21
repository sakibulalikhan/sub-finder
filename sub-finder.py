import requests 
import sys 
import resolver
import threading
import time

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
print("\n* Linkedin: https://www.linkedin.com/in/sakibulalikhan         *")
print("\n****************************************************************")
print("\n")

domain = input("Enter domain name: ")


def check_host(self, host):
    is_valid = False
    Resolver = dns.resolver.Resolver()
    Resolver.nameservers = ['1.1.1.1', '1.0.0.1']
    self.lock.acquire()
    try:
        ip = Resolver.query(host, 'A')[0].to_text()
        if ip:
            if self.verbose:
               self.print_("%s%s: %s%s" % (R, self.engine_name, W, host))
               is_valid = True
               self.live_subdomains.append(host)
    except:
        pass
        self.lock.release()
        return is_valid


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


def domain(self):
    time.sleep(0.2)

def __domain__(self):
    t = threading.Thread(target=self.domain)
    t.start()
