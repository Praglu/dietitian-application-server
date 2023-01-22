FROM node:18-alpine

EXPOSE 5173

WORKDIR /app

COPY /src/frontend/package.json /src/frontend/package-lock.json ./

RUN npm install --silent

COPY /src/frontend ./

CMD ["npm", "start"]
