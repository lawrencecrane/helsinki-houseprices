FROM alpine

RUN apk update && apk add sqlite && mkdir /data

WORKDIR /home/sqlite

COPY sqlite/create_db.sql .
COPY sqlite/create.sh .

CMD ["/home/sqlite/create.sh"]
