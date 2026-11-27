```bash

# install litellm 
> pip install 'litellm[proxy]' primsa --break-system-packages

# start the litellm using the config.yaml file
> litellm --config config.yaml --port 4000

# create a postgres db container
> docker container run -itd --name postgres -e POSTGRES_USER=litellm -e POSTGRES_PASSWORD=litellm -e POSTGRES_DB=litellm -p 5432:5432 postgres:alpine

```