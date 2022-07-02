import os

import requests
from dotenv import load_dotenv


def main():
    load_dotenv()
    bitly_token = os.getenv('bitly_token')

    url = 'https://api-ssl.bitly.com/v4/user'

    headers = {
        'Authorization': f'Bearer {bitly_token}',
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print(response.text)


if __name__ == '__main__':
    main()
