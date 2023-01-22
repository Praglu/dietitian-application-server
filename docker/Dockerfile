FROM node:18-alpine

WORKDIR /app

COPY /src/frontend/package.json /src/frontend/package-lock.json ./

RUN npm install --silent

COPY /src/frontend ./

EXPOSE 3000

CMD ["npm", "start"]
