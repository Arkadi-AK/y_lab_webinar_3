# webinar_num_3

## Установка
```bash
python3 -m venv venv
. venv/bin/activate
cd not_service
pip install -r requirements.txt
```
Переименуйте файл "exsample.env" в ".env" и введите необходимые данные.


## Запуск проекта в docker контейнере

* Создание и сборка контейнеров # ```sudo docker-compose up --build```
* Запуск командной строки в контейнере приложения # ```sudo docker-compose exec ylab_app bash```
* Применение миграции # ```alembic upgrade head```


## Использование
* http://127.0.0.1:8000/api/v1/posts # просмотр списка постов
* http://127.0.0.1:8000/api/v1/signup # регистрируется на сайте
* http://127.0.0.1:8000/api/v1/login # Заходит на сайт
* http://127.0.0.1:8000/api/v1/refresh # Обновляет токен
* http://127.0.0.1:8000/api/v1/users/me # Смотрит свой профиль
* http://127.0.0.1:8000/api/v1/posts # Создает пост
* http://127.0.0.1:8000/api/v1/users/me # Обновляет информацию о себе
* http://127.0.0.1:8000/api/v1/logout # Выйти из аккаунта
* http://127.0.0.1:8000/api/v1/login # Повторно заходит на сайт
* http://127.0.0.1:8000/api/v1/logout_all # Выйти со всех устройств