# Рещение тестового задания

Полное описание тестового задания приведено [по данному адресу](https://github.com/DonKoteyka/test_task_6/blob/main/Task.docx)

В исходном состянии предполагается что на устройстве для запуска данного приложения  установлен python, postgresql, либо docker. 

Данная инструкция описывает запуск с помощью docker, для чего нужно:
1.   Скопировать архив на устройство с помощью сайта [github](https://github.com/DonKoteyka/test_task_6/) в виде `.zip` архива и распоаковать, либо склонировать с помощью `git` командой:
```bash git clone https://github.com/DonKoteyka/test_task_6.git```

2.  Создать в папке `test_task_6`  файл `.env`со следующими переменныим:
```
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin
POSTGRES_DB=test
POSTGRES_PORT=5432
POSTGRES_HOST=db
```
3.  Находясь в папке `test_task_6` выполнить следующие комманды:
```bash docker-compose up --build -d ``` 

В случае использования ОС на базе Linux в начале команды следует добвать `sudo`.
После успешной сборки образа выполнить следующие комманды

- ```bash docker-compose exec -it python manage.py migrate ```
- ```bash docker-compose exec -it python manage.py collectstatic ```

В результате запущенное приложение должно работать по адресу `http://localhost/`. В данный момент приложение развёрнуто на сервере и доступно по адресу
`http://89.111.174.10/`

В данном API реализованы следующие пути:

- `admin/` - стандартная админка Django, вход осуществляется по `"email", "password"` пользователя созданного в том числе и через API

- `api/auth/user/` - созданиие пользователя принимает `JSON` со следующими переменныим для регистраци `"first_name", "last_name", "email", "password"`, в тестовых целях доступно создание администратора, для этого нужно передать дополнительно `"admin": "True"`

- `api/auth/` - авторизация уже созданного пользователя, нужны следующие переменные `"email", "password"`, возвращает токен для дальнейшей работы

- `api/news/` - принимает запросы на создание, редактирование и удаление статей от пользователей (с токеном), либо чтение без токена, необходимые поля для комментария `"title", "description"`

- `api/news/1/comments/` - принимает запросы на создание, редактирование и удаление комментарие для статьи `1` от пользователей (с токеном), необходимые поля `"post", "comment"`

- `api/news/1/like/` - принимает запросы на оставление лайков для статьи `1` от пользователей(с токеном)
