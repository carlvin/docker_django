# Fetch the latest Nginx image
#FROM jwilder/nginx-proxy:alpine
FROM nginxproxy/nginx-proxy:alpine
COPY vhost.d/default /etc/nginx/vhost.d/default
COPY custom.conf /etc/nginx/conf.d/custom.conf
    