docker build -t sqlite-db-creator -f sqlite/Dockerfile .
docker build -t seleniumserver-sidecar -f seleniumserver/Dockerfile .
docker build -t html-scraper .
