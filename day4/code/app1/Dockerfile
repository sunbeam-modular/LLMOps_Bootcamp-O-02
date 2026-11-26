FROM httpd:alpine
COPY index.html /usr/local/apache2/htdocs/

# use this for ubuntu based image
# RUN useradd --system app

# use this for alpine based image
RUN adduser -S -H app
USER app
