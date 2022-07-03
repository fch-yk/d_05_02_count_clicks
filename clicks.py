import os
import sys
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv


def is_bitlink(link, token):
    parsed_link = urlparse(link)
    bitlink = f'{parsed_link.hostname}{parsed_link.path}'
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}'
    url = url.format(bitlink=bitlink)
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.ok


def count_clicks(token, link):
    parsed_link = urlparse(link)
    bitlink = f'{parsed_link.hostname}{parsed_link.path}'
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    url = url.format(bitlink=bitlink)
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['total_clicks']


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
    user_input = input('Input link: ')
    try:
        link_is_bitlink = is_bitlink(user_input, token)
    except requests.exceptions.HTTPError:
        link_is_bitlink = False

    if link_is_bitlink:
        try:
            total_clicks = count_clicks(token, user_input)
        except requests.exceptions.HTTPError as error:
            print(
                f'Anable to count total clicks. Error: {error}',
                file=sys.stderr
            )
            sys.exit()
        else:
            print('Total clicks: ', total_clicks)
    else:
        try:
            bitlink = shorten_link(token, user_input)
        except requests.exceptions.HTTPError as error:
            print(f'Incorrect link. Error: {error}', file=sys.stderr)
            sys.exit()
        else:
            print('Bitlink: ', bitlink)


if __name__ == '__main__':
    main()
