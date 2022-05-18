# leve-teste Backend (BE)

## Requisitos
Python 3.9.5

### Dependencias
Para instalar as dependencias é necessário entrar na pasta do projeto "leveTeste" e usando um terminal de sua preferência rodar o seguinte comando:
```
pip install -r Requirement.txt
```


## Criar Models e DB
Para criar os modelos e DB é necessário entrar na pasta do projeto "leveTeste" e usando um terminal de sua preferência rodar os seguintes comandos:

**makemigration**
```
python manage.py makemigrations api 
```
Que criará os seguintes arquivos:
* ./d.sqlite3
* ./api/migrations/__init__.py
* ./api/migrations/0001_initial.py

E terá a seguinte saída no terminal:
```
❯ python manage.py makemigrations api
Migrations for 'api':
  api/migrations/0001_initial.py
    - Create model Salaries
    - Create model User
```

**migrate**
```
python manage.py migrate
```
Que terá a seguinte saída no terminal:
```
❯ python manage.py migrate           
Operations to perform:
  Apply all migrations: admin, api, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying api.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

## Iniciar o servidor
Para iniciar o servidor BE é necessário entrar na pasta do projeto "leveTeste" e usando um terminal de sua preferência rodar o seguinte comando:
```
python manage.py runserver
```

Quando o BE estiver pronto você verá está mensagem:
```
❯ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 18, 2022 - 00:34:58
Django version 4.0.4, using settings 'leveTest.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
E o endereço do servidor será: http://127.0.0.1:8000/

## Frontend
Agora vamos para o frontend: [Leve-app](https://github.com/HevertonLemos/leve-app)
