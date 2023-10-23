import os
from concurrent.futures import ThreadPoolExecutor
from requests import get
import argparse
from tqdm import tqdm

Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Wh = '\033[1;37m'
os.system('clear')

parser = argparse.ArgumentParser(description='zfuzz tool For fuzzing Web Site ')
parser.add_argument('-u', help='Target Url')
parser.add_argument('-w', '--wordlist', help='word list for fuzzing ')
args = parser.parse_args()
site = "" + args.u
wordlist = args.wordlist

with open(wordlist, "r") as file:
    urls = file.read().splitlines()

def check_url(url):
    address = site + "/" + url
    response = get(address)
    if response.status_code == 200:
       print(f'{Gr} [+] Page Found: {address}')
    else:
         a = ''
with ThreadPoolExecutor() as executor:
        results = list(tqdm(executor.map(check_url, urls), total=len(urls)))