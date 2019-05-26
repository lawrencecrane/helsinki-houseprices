docker run -it --name dev-vuokraovi-frontend \
           -v $(pwd)/frontend/src:/home/node/vuokraovi/src \
           -v $(pwd)/frontend/src-gen:/home/node/vuokraovi/src-gen \
           --rm dev-vuokraovi-frontend $@
