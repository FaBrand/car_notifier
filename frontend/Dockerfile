# Stage 0 - Build App
FROM node:alpine as builder
RUN npm set progress=false && npm install -g @angular/cli

WORKDIR /app

COPY ./car-notifier-app/package*.json /app/
RUN npm install

COPY ./car-notifier-app /app

RUN ng build --aot --prod

# Stage 1 - nginx server
FROM nginx:alpine as server
ENV site=car_notifier

RUN rm -rf /var/www/
RUN rm -rf /usr/share/nginx/html
RUN mkdir -p /var/www/$site/html

COPY --from=builder /app/dist/car-notifier-app/* /var/www/$site/html/

EXPOSE 80 443
