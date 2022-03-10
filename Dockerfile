FROM python:3.7-alpine

COPY main.py /tmp
COPY last_mention.py /tmp
COPY tweets.py /tmp
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /tmp
CMD ["python3", "main.py"]