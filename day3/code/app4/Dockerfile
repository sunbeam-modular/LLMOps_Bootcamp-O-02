FROM httpd
COPY index.html /usr/local/apache2/htdocs/
EXPOSE 80
HEALTHCHECK --interval=10s --start-period=10s --timeout=5s CMD curl http://localhost:80
