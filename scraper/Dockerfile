FROM python:3.7-slim

WORKDIR /home/src

# install Chrome:
RUN apt-get update && apt-get install -y wget gnupg libpango1.0-0 unzip
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list'
RUN apt-get update && apt-get install -y google-chrome-stable

# get chromedriver:
RUN wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE -O /tmp/version \
    && version_number=`cat /tmp/version` \
    && wget https://chromedriver.storage.googleapis.com/${version_number}/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && mv chromedriver /usr/local/bin/ \
    && rm chromedriver_linux64.zip

RUN pip install --upgrade pip
RUN pip install beautifulsoup4 selenium

COPY src/ .

CMD ["python", "./houseprice_scraper.py"]
