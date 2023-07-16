# Fetch the latest Nginx image
FROM nginx:latest
# Remove default nginx.conf
RUN rm /etc/nginx/conf.d/default.conf
# Copy our custom nginx.conf
COPY nginx.conf /etc/nginx/conf.d

