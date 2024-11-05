# Автор
Над проектом работал Афанасьев Александр
# Технологии и их версии:
В проекте использовались такие технологии, как:
- asgiref==3.7.2
- backports.zoneinfo==0.2.1
- certifi==2024.8.30
- cffi==1.15.1
- charset-normalizer==3.4.0
- coreapi==2.3.3
- coreschema==0.0.4
- cryptography==43.0.3
- defusedxml==0.8.0rc2
- Django==3.2.25
- django-templated-mail==1.1.1
- djangorestframework==3.15.1
- djangorestframework-simplejwt==4.7.2
- djoser==2.1.0
- idna==3.10
- importlib-metadata==1.7.0
- itypes==1.2.0
- jinja2==3.1.4
- MarkupSafe==2.1.5
- oauthlib==3.2.2
- pycparser==2.21
- PyJWT==2.8.0
- python3-openid==3.2.0
- pytz==2024.2
- requests==2.31.0
- requests-oauthlib==2.0.0
- six==1.16.0
- social-auth-app-django==4.0.0
- social-auth-core==4.4.2
- sqlparse==0.4.4
- typing-extensions==4.7.1
- uritemplate==4.1.1
- urllib3==2.0.7
- zipp==3.15.0

## Как запустить проект:
1. Клонировать репозиторий командой:
```
git clone <ссылка на репозиторий>.
```

2. Создать и активировать виртуальное окружении в корневой директории проекта:
    ```
    python -m venv venv
    ``` 
    
    ```
    source venv/Scripts/activate
    ``` 

3. Установить зависимости командой:
```
pip install -r requirements.txt
```

4. Выполните миграции командой:
```
python manage.py migrate
```

5. Выполните команду для запуска dev-сервера 😹
```
python manage.py runserver
```

## Эндпоинты для взаимодействия с ресурсами:
1.  Получить список всех постов (GET):
http://127.0.0.1:8000/api/posts/

2.  Получить определенный пост (GET):
http://127.0.0.1:8000/api/posts/1/

3.  Создать новый пост (POST): (Требуется аутентификация)
http://127.0.0.1:8000/api/posts/
