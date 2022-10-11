FROM node:14.11.0-alpine

WORKDIR /usr/src/app

RUN rm -rf /usr/src/app/node_modules

RUN mkdir -p /usr/src/app/node_modules

RUN chown -R node:node /usr/src/app

RUN yarn global add @vue/cli

USER node

COPY ./vuejs/package*.json ./vuejs/yarn.lock ./

RUN yarn install --frozen-lockfile --check-files

COPY --chown=node:node ./vuejs/ /usr/src/app/

CMD yarn build --dest build-output && \
    rm -rf ./dist && \
    cp -r ./build-output ./dist
