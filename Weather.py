#!/usr/bin/env python

imporet os
impore requests
import sys

from argparse import ArgumentParser

parser = ArgumentParser(description='Get the current weather inforamation')
parser.add_argument('zip', help='zip/postal code to get the weather for')
parser.add_argument('---country', default='india', help='country zip/postal belongs default is "india"')
args = parser.parse_args()
api_key = os.getenv('QWM_API_KEY')
if not api_key:
    print("Error: no 'OWM_API_KEY' provided")
    sys.exit(1)
url = f"http://api.openweathermap.org/data/2.5/weather?zip={args.zip},{args.country}&appid={api_key}"
res = requests.get(url)

if res.status_code != 200:
    print(f"Error talking to weather provider:  {res.status_code}")
    sys.exit(1)

print(res.json())