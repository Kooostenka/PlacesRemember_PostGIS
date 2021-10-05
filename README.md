# Places Remember

Веб-приложение, с помощью которого люди могут хранить свои впечатления о посещенных местах.

### Как установить

- Запустите проект с помощью следующих команд:
```
docker-compose build
docker-compose up
```

- Для авторизации пользователей с помощью VK, создайте приложение на сайте https://vk.com/dev
- Далее перейдите на сайт администратора Django, добавьте приложение в "Social applications" и в "Sites" замените example.com на http://0.0.0.0:8000/:
```
http://0.0.0.0:8000/admin
Логин: admin
Пароль: admin
```