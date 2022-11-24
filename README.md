<h1 align="center">Stripe</h1>

![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)

# Описание сервиса
Платежная система.<br>
# Установка
1. Клонируйте репрозиторий ```https://github.com/spqr-86/mini_library```
2. Создайте файл .env по примеру env.example.
3. Установите Docker (https://docs.docker.com/engine/install/)
4. Выполните ```docker-compose up -d --build```
5. Выполните:<br>
  ```docker-compose exec web python manage.py createsuperuser```<br>
6. Теперь проект доступен по адресу http://localhost/

# Технологии
* Python
* Django
* Stripe API
* Docker

# Проект разработал:
* [Петр Балдаев](https://github.com/spqr-86)

