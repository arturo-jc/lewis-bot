# lewis-bot

## Live link

https://twitter.com/DavidLewisBot

## About

This is a bot that replies to mentions with quotes from David Lewis's masterpiece *On The Plurality of Worlds*.

## Installation

Fork and clone:

```
git clone https://github.com/arturo-jc/lewis-bot
```

Navigate to the project folder and create a virtual environment:

```
python -m venv env
```

Activate the virtual environment and install dependencies:


```
source env/Scripts/activate
pip install -r requirements.txt
```

## Usage

To serve locally, add your own Twitter credentials to a `.env` file then run:

```
python application.py
```

To extract tweets from a different book, copy a pdf of the book into the project folder and then in `extract.py`, set:

```
DOCUMENT = 'filename.pdf'
```

Finally, run:
```
python extract.py
```

## Built with

* Python
* Flask
* Tweepy