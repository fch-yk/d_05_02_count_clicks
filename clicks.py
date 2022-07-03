import os
import sys

import requests
from dotenv import load_dotenv


def shorten_link(token, link):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/'
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'long_url': link}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()['link']


def main():
    load_dotenv()
    token = os.getenv('bitly_token')
    link = input('Input link: ')
    try:
        bitlink = shorten_link(token, link)
    except requests.exceptions.HTTPError as error:
        print(f'Incorrect link. Error: {error}', file=sys.stderr)
        sys.exit()

    print('Битлинк', bitlink)


if __name__ == '__main__':
    main()
