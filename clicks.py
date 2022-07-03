import os

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
    print('Битлинк', shorten_link(token, link))


if __name__ == '__main__':
    main()
