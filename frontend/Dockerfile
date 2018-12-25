# Stage 0 - Build App
FROM node as builder

ADD ./car-notifier-app /usr/src/app
WORKDIR /usr/src/app

RUN npm set progress=false && npm install

# Stage 1 - nginx server
FROM nginx as server
ENV site=car_notifier

RUN rm -rf /var/www/
RUN rm -rf /usr/share/nginx/html
RUN mkdir -p /var/www/$site/html

COPY --from=builder /usr/src/app/dist/car-notifier-app/* /var/www/$site/html/

ADD ./nginx/conf/sites-available/$site /etc/nginx/sites-available/$site
ADD ./nginx/conf/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443

