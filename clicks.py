import os

import requests
from dotenv import load_dotenv


def main():
    load_dotenv()
    bitly_token = os.getenv('bitly_token')
    url = 'https://api-ssl.bitly.com/v4/bitlinks/'
    headers = {'Authorization': f'Bearer {bitly_token}'}
    payload = {'long_url': 'https://www.youtube.com/'}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    print(response.json()['link'])


if __name__ == '__main__':
    main()
