# Build
sudo docker build -t houseprice-scraper .

# Run
sudo docker run -v $(pwd)/src:/home/src --rm houseprice-scraper
