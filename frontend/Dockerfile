# Stage 0 - Build App
FROM node:alpine as builder
RUN npm set progress=false && npm install -g @angular/cli

WORKDIR /app

COPY ./car-notifier-app/package*.json /app/
RUN npm install

COPY ./car-notifier-app /app

RUN ng build --aot --prod --output-path dist

# Stage 1 - nginx server
FROM node:alpine as site_Data

COPY --from=builder /app/dist/* /app/site-data/
