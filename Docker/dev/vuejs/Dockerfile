FROM node:14.11.0-alpine

WORKDIR /usr/src/app

RUN rm -rf /usr/src/app/node_modules

RUN mkdir -p /usr/src/app/node_modules

RUN chown -R node:node /usr/src/app

RUN npm install -g @vue/cli

COPY --chown=node:node ./vuejs/ /usr/src/app/

RUN npm install --check-files

RUN npm install vue-the-mask

RUN npm install vuetify@2.6.12



EXPOSE 8080