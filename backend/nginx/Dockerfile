FROM nginx:alpine

RUN rm -rf /var/www/
RUN rm -rf /usr/share/nginx/html

ADD nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443
