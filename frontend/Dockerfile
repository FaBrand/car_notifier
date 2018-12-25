# Stage 0 - Build App
FROM node:alpine as builder
RUN npm set progress=false && npm install -g @angular/cli

WORKDIR /usr/src/app

ADD ./car-notifier-app/package.json /usr/src/app
ADD ./car-notifier-app/package-lock.json /usr/src/app

ADD ./car-notifier-app /usr/src/app
RUN ng build --aot

# Stage 1 - nginx server
FROM nginx:alpine as server
ENV site=car_notifier

RUN rm -rf /var/www/
RUN rm -rf /usr/share/nginx/html
RUN mkdir -p /var/www/$site/html

COPY --from=builder /usr/src/app/dist/car-notifier-app/* /var/www/$site/html/

EXPOSE 80 443
