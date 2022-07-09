# Count clicks

The program uses [The Bitly API](https://dev.bitly.com/) for

- transforming a long link into a short one
- getting total clicks of a short link

## Prerequisites

Python 3.10 or higher required.

## Installing

- Download the project files
- It is recommended to use [venv](https://docs.python.org/3/library/venv.html?highlight=venv#module-venv) for project isolation
- Set up packages:

```bash
pip install -r requirements.txt
```

- Set up `dotenv` [command line interface](https://github.com/theskumar/python-dotenv#command-line-interface):

```bash
pip install "python-dotenv[cli]"
```

- Set up an environmental variable `BITLY_TOKEN`:

```bash
dotenv set BITLY_TOKEN token
```

where `token` is your access token that you can get [here](https://dev.bitly.com/).
The access token provides the possibility to use [The Bitly API](https://dev.bitly.com/).

## Running script

- Run:

```bash
python clicks.py link
```

where `link` is a web link (short or long).

The output for a long link (e.g., [google.com](https://www.google.com/)) is a short link.
The output for a short link (e.g., [bit.ly/3ny2HtI](https://bit.ly/3ny2HtI)) is total clicks.

## Project purposes

The project was created for educational purposes.
It's a lesson for python and web developers at [Devman](https://dvmn.org)
