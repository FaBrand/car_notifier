FROM nginx

ENV site=car_notifier

RUN rm -rf /var/www/
RUN rm -rf /usr/share/nginx/html
RUN mkdir -p /var/www/$site/html

ADD ./nginx/content/index.html /var/www/$site/html
ADD ./nginx/conf/sites-available/$site /etc/nginx/sites-available/$site
ADD ./nginx/conf/nginx.conf /etc/nginx/nginx.conf
