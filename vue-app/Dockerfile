FROM node:15.8.0-alpine3.10

RUN apk update && apk add bash

WORKDIR /vue-app
COPY ./package.json ./yarn.lock /vue-app/
ENV PATH /vue-app/node_modules/.bin:$PATH

RUN yarn

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=5000

COPY . /vue-app
RUN yarn build
CMD ["yarn", "start"]