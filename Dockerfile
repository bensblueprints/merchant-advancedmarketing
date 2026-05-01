FROM node:20-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN mkdir -p /data
VOLUME ["/data"]
EXPOSE 80
CMD ["node", "server.js"]
