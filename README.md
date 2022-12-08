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

## API Docs

### Structure Data
```
inn: CharField # Инн
company_name: CharField # Название компании
contact_number: CharField # Номер телефона

addresses: JSONField # Объект 

supreme_management_body: CharField # Высший орган управления
supreme_management_person: CharField # Руководитель
supreme_management_inn: CharField # Руководитель ИНН

is_supervisoty: BooleanField # Наличие коллегиального исполнительного органа
supervisoty_board_persone_name: CharField # Наименование коллегиального исполнительного органа
list_supervisoty_board_persone: JSONField # Члены наблюдательного совета

is_collegiate_body: BooleanField # Наличие наблюдательного совета
collegiate_person: CharField # Наименование наблюдательного совета
list_collegial_executive_body: JSONField # Члены коллегиального исполнительного органа

employers_volume: CharField # Численность персонала
salary_debt: BigIntegerField # Задолженность по з/п

company_group_name: CharField # Название группы компаний
start_date: DateField # Дата начала действия
end_date: DateField # Дата окончания действия
group_members: JSONField # Состав группы компаний

beneficiaries: CharField # Выгодоприобретатели

planned_operations: JSONField # Сведения о планируемых операциях по счету

account_operations: JSONField # Сведения о целях установления деловых отношений с банком
operation_volume: CharField # Количество операций по безналичным платежам в месяц
sum_per_month: CharField # Сумма операций по снятию наличности в месяц
cash_source: JSONField # Источники происхождения денежных средств
outside_contracts_volume: CharField # Количество операций по внешнеторговым контрактам в месяц
state_employers: CharField # Штатная численность сотрудников

information_goals: JSONField # Отметьте все верные утверждения

tariff: CharField # Тариф
is_finished: BooleanField
last_step: CharField
```
### Addresses structure
```
{
  addresses: [
    {
      typeAdress: enum('Юридический', 'Фактический', 'Почтовый'),
      legal_address: str, # Юридический адрес
      physic_address: str, # Фактический адрес
      mail_address: str, # Почтовый адрес
      basis: str, # Основание
      address: str, # Адрес
    }
  ]
}
```

### Supervisory body and collegiate body
```
{
  account_onw_role: enum('Учредитель', 'Бенефициарный владелец', 'Подписант'),
  account_own_gender: str # Пол
  account_own_lastname: str # Фамилия
  account_own_name: str # Имя
  account_own_surname: str # Отчество

  account_onw_inn: str # Инн
  account_own_citizenship: str # Гражданство
  account_own_phone: str # Номер телефона
  account_own_piece: str # Доля владения
  account_own_snils: str # СНИЛС (при наличии)

  is_person_a_foreign_public: enum('Да', 'Нет') # Является ли лицо иностранным публичным должностным лицом либо лицом, связанным с таковым родственными,
            партнерскими или иными отношениями?

  account_own_registration: str # Адрес регистрации
  assigned_publ_pers_registraion: str # Адрес регистрации
  assigned_publ_pers_relation: enum('Супруг', 'Супруга') # Степень родства

  accownt_own_living: str | enum('Совпадает') # Адрес фактического проживания

  account_own_mail: str #  Почтовый адрес

  first_passport_page_url: str # URL на паспорт

  account_birth_place: str # Место рождения
  account_datebirth: date # Дата рождения
  date_issue: date # Дата выдачи
  division_code: str # Код подразделения (при наличии)
  doc_number: str # Номер документа удостоверяющего личность
  doc_serial: str # Серия документа удостоверяющего личность
  doc_type: enum('Паспорт') # Тип документа
  issued_by: str # Кем выдан
  validity: date # Срок действия

}
```
### Group members
```
[
  {
    name: str,
    inn: str,
    ogrn: str,
  },
]
```
### Planned operations
```
[
  'Договор купли-продажи (товарный)',
  'Агентский договор',
  'Договор комиссии',
  'Договор купли-продажи ценных бумаг',
  'Договор аренды',
]
```

### Account operations
```
[
  'Дистанционное банковское обслуживание',
  'Внешнеэкономические операции',
  'Интернет-эквайринг',
  'Кредитование',
  'Торговый эквайринг',
  'Переводы СБП (c2b)',
]
```

### Account operations
```
[
  'Дистанционное банковское обслуживание',
  'Внешнеэкономические операции',
  'Интернет-эквайринг',
  'Кредитование',
  'Торговый эквайринг',
  'Переводы СБП (c2b)',
]
```

### Cash source
```
[
  'Средства, полученные в рамках осуществляемой хозяйственной деятельности',
  'Собственные средства',
  'Заемные средства (займы от третьих лиц, учредителей и т.д)',
  'Иные',
]
```


### Send and get loan-application

```
URL: /api/loan-application/current/<str:phone_number>/
```
GET method 
> Body
```
{}
```
> Return
```
'status',
'inn',
'company_name',
'contact_number',

'addresses',

'supreme_management_body',
'supreme_management_person',
'supreme_management_inn',

'is_supervisoty',
'supervisoty_board_persone_name',
'list_supervisoty_board_persone',

'is_collegiate_body',
'collegiate_person',
'list_collegial_executive_body',

'employers_volume',
'salary_debt',

'company_group_name',
'start_date',
'end_date',
'group_members',

'beneficiaries',

'planned_operations',

'account_operations',
'operation_volume',
'sum_per_month',
'cash_source',
'outside_contracts_volume',
'state_employers',

'tariff',
'is_finished',
'last_step',
'created_at',
```


POST method create or updates the data. If is_finished = False 
then update data, and if is_finished = True then create data
> body
```
'inn',
'company_name',
'contact_number',

'addresses',

'supreme_management_body',
'supreme_management_person',
'supreme_management_inn',

'is_supervisoty',
'supervisoty_board_persone_name',
'list_supervisoty_board_persone',

'is_collegiate_body',
'collegiate_person',
'list_collegial_executive_body',

'employers_volume',
'salary_debt',

'company_group_name',
'start_date',
'end_date',
'group_members',

'beneficiaries',

'planned_operations',

'account_operations',
'operation_volume',
'sum_per_month',
'cash_source',
'outside_contracts_volume',
'state_employers',

'tariff',
'is_finished',
'last_step',
```
> return
```
{}
```


### upload file
POST method send file in FormDate
```
/api/passport-load/
```
> body
```
passport: typeFile
```
> return
```
{
  path: "<URLFile>"
}
```

### Get phone number by telegram chat id
GET method
```
api/get_phone/<str:telegram_chat_id>/
```
> return
```
{
  phone: '722222222222'
}
```

### Check phone number
GET method
```
api/user/<str:telegram_chat_id>/
```
> return
```
If there is telegram_chat_id then status 200
If not telegram_chat_id then status 404
```

POST method
```
api/user/<str:telegram_chat_id>/
```
> body
```
{
  phone_number: '79091233342'
}
```
```
If success then status 200
If error then status 400
```

### License 
GET method
```
api/get_license/
```
> return 
```
{
  view,
  number,
  Issued_by,
  License_issue_date,
  Validity,
  List_types_licensed_activities,
}
```


### Status list
GET method
```
api/loan-application/<int:telegram_chat_id>/
```
> return

Array "Structure Data"

