FROM registry.hub.docker.com/library/node:16-alpine as base

ENV APP_DIR /frontend

COPY . ${APP_DIR}
WORKDIR ${APP_DIR}

RUN npm install
RUN npm run build

CMD ["npm", "run", "preview"]