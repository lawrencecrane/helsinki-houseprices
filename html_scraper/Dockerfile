FROM python:alpine3.9

RUN pip install selenium beautifulsoup4

WORKDIR /home/selenium

COPY src .

CMD ["python", "/home/selenium/scrape.py"]
