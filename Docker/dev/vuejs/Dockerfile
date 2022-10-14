FROM node:14.11.0-alpine

WORKDIR /usr/src/app

RUN rm -rf /usr/src/app/node_modules

RUN mkdir -p /usr/src/app/node_modules

RUN chown -R node:node /usr/src/app

RUN yarn global add @vue/cli

COPY ./vuejs/package*.json ./vuejs/yarn.lock ./

RUN yarn install --check-files

RUN yarn add vue-the-mask

COPY --chown=node:node ./vuejs/ /usr/src/app/
