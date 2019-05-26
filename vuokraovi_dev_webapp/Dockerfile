# === frontend dev end & assets builder
FROM node as dev-vuokraovi-frontend

WORKDIR /home/node/vuokraovi

RUN npm install -g browserify \
    && npm install -g uglify-js \
    && npm install -g gulp-cli

COPY frontend ./

RUN npm install && npm run build

CMD ["gulp", "build-vuokraovi"]


# === backend web server
FROM nginx as dev-vuokraovi-app

RUN rm /etc/nginx/conf.d/*

COPY --from=dev-vuokraovi-frontend /home/node/vuokraovi/src-gen /usr/share/vuokraovi/www/
COPY nginx/vuokraovi.conf /etc/nginx/conf.d/vuokraovi.conf
