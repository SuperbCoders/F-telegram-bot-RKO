# loan-application-bot

## To run the development build

```
(cd ./Docker/dev && sudo docker-compose up --build)
```

## To run the production build

```
(cd ./Docker/prod && sudo docker-compose up --build -d)
```

## Tools and services

### Docker

The project uses Docker to run all the needed services in separate isolated containers and Docker Compose that allows to combine and run these containers together.

#### Development

`./Docker/dev` directory contains Docker development configuration which is used to run the project locally.

- `./Docker/dev/docker-compose.yaml` - Docker Compose configuration
- `./Docker/dev/python` - a custom Docker image that's used to run Django and Celery processes
- `./Docker/dev/vuejs` - a custom Docker image that's used to run Vue CLI commands
- `./Docker/dev/.env` - contains environment variables used by different Docker containers
- `./Docker/dev/.env.secret` - contains secret environment variables which can't be submitted to a code repository

#### Production

`./Docker/prod` directory contains Docker production configuration which is used to run the project on the server. It is different from the local configuration, eg.: all the services are set to be automatically restarted and VueJS container is set to build the production asset bundle instead of running a local development server.

- `./Docker/prod/docker-compose.yaml` - Docker Compose configuration
- `./Docker/prod/python` - a custom Docker image that's used to run Django and Celery processes
- `./Docker/prod/vuejs` - a custom Docker image that's used to run Vue CLI commands
- `./Docker/prod/.env` - contains environment variables used by different Docker containers
- `./Docker/prod/.env.secret` - contains secret environment variables which can't be submitted to a code repository

### Django

The project uses [Django](https://docs.djangoproject.com/en/3.1/) application with the [REST framework](https://www.django-rest-framework.org/) as a back-end API.

### Celery

The project uses Celery ([http://docs.celeryproject.org/en/latest/index.html](http://docs.celeryproject.org/en/latest/index.html)) to run asynchronous tasks with Python.

The Celery process is using RabbitMQ running in a separate Docker container as a broker ([https://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html](https://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html)).

`./django/apps/main/tasks.py` contains all the Celery tasks and related functions.

### Vue

The project uses VueJS as a front-end framework. The single-page application built with VueJS is being used by Telegram bot utilizing Telegram's web-app API [https://core.telegram.org/bots/webapps](https://core.telegram.org/bots/webapps).

- [https://vuejs.org/v2/guide/](https://vuejs.org/v2/guide/) - general introduction
- [https://vuejs.org/v2/guide/single-file-components.html](https://vuejs.org/v2/guide/single-file-components.html) - single-file components basics

#### Vue CLI

The front-end for the project is created and managed using Vue CLI ([https://cli.vuejs.org/guide/](https://cli.vuejs.org/guide/)).

### Telegram bot

The Telegram bot is build with Python by using the `python-telegram-bot` wrapper for Telegram's bot API. ([https://github.com/python-telegram-bot/python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot))

## Config

### ./Docker/prod/.env

- `COMPOSE_PROJECT_NAME` - project's name for the Docker Compose
- `DOMAIN_NAME` - the Django API domain name
- `ALLOWED_CLIENT_DOMAIN_NAME` - the client domain name added to the CORS whitelist by Django [https://github.com/adamchainz/django-cors-headers](https://github.com/adamchainz/django-cors-headers)
- `DJANGO_SETTINGS_MODULE` - the Django settings module used by Celery
- `VUE_APP_API_ROOT_URL` - the API root URL used by the VueJS client

### ./Docker/prod/.env.secret

- `SECRET_KEY` - the Django secret key [https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key](https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key)
- `TELEGRAM_BOT_API_TOKEN` - Telegram's API token [https://core.telegram.org/bots#6-botfather](https://core.telegram.org/bots#6-botfather)

## Setting up a new server

### Server

Create a new user

`adduser loan-application-bot`

Add the new user to the sudo group

`usermod -aG sudo loan-application-bot`

Log in and continue working on the server as the new user after that.

### Nginx

Install Nginx

```
sudo apt update
sudo apt install nginx
```

To avoid a possible hash bucket memory problem that can arise from adding additional server names, it is necessary to adjust a single value in the `/etc/nginx/nginx.conf` file. Open the file:

`sudo nano /etc/nginx/nginx.conf`

Find the `server_names_hash_bucket_size` directive and remove the `#` symbol to uncomment the line.

The initial Nginx config:

```
server {
    listen 80;
    listen [::]:80;
    server_name [your_domain/api.your_domain];
    return 200;
}
```

Create files with the initial config for the client and API domains:

```
sudo nano /etc/nginx/sites-available/your_domain
sudo ln -s /etc/nginx/sites-available/your_domain /etc/nginx/sites-enabled/
sudo nano /etc/nginx/sites-available/api.your_domain
sudo ln -s /etc/nginx/sites-available/api.your_domain /etc/nginx/sites-enabled/
```

Check the configuration and restart Nginx to enable your changes:

```
sudo nginx -t
sudo systemctl restart nginx
```

### Let's encrypt

Install Certbot and it’s Nginx plugin with apt:

`sudo apt install certbot python3-certbot-nginx`

Create SSL certificates for both of your domains:

```
sudo certbot --nginx -d your_domain
sudo certbot --nginx -d api.your_domain
```

After that replace the initial Nginx configuration for your domains with the production-ready one. Examples could be found at `./config/examples/nginx/`

```
sudo nano /etc/nginx/sites-available/your_domain
sudo nano /etc/nginx/sites-available/api.your_domain
sudo systemctl restart nginx
```

### Project

Create a new directory and navigate to it:

```
mkdir projects
cd ~/projects
```

Install git and clone the project repository

```
sudo apt install git
git clone https://github.com/SuperbCoders/F-telegram-bot-application
```

Navigate to the project root and create the `.env.secret` file:

```
cd loan-application-bot/
touch ./Docker/prod/.env.secret
nano ./Docker/prod/.env.secret
```

### Docker

Install packages to allow apt to use a repository over HTTPS

```
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

Add Docker’s official GPG key

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```

Use the following command to set up the stable repository

```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Install Docker Engine

```
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

Install Docker Compose

```
sudo apt install docker-compose
```

Start containers with Docker Compose

```
(cd ./Docker/prod && sudo docker-compose up --build -d)
```

### Admin page setup

Create a new admin user

```
(cd ./Docker/prod/ && sudo docker-compose exec django python manage.py createsuperuser --settings=project.settings.production)
```

### Checking logs

```
(cd ./Docker/prod/ && sudo docker-compose logs)
```

## Updating the application on the server

Get the latest version from the repository

```
git pull origin master
```

Restart the Docker Compose

```
(cd ./Docker/prod && sudo docker-compose up --build -d)
```

## Contact info

Alex Barabash (alex@baraba.sh)
