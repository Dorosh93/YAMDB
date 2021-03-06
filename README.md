# Описание проекта YaMDb
Проект YaMDb собирает отзывы пользователей на произведения. Произведения делятся на категории: «Книги», «Фильмы», «Музыка».
Список категорий может быть расширен администратором.

Сами произведения в YaMDb не хранятся, в нём можно поделиться впечатлением.

В каждой категории есть произведения: книги, фильмы или музыка.
Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» 
и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха.
Произведению может быть присвоен жанр из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).
Новые жанры может создавать только администратор.
Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы 
и ставят произведению оценку в диапазоне от одного до десяти (целое число); 
из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). 
На одно произведение пользователь может оставить только один отзыв.

## Пользовательские роли
1. Аноним — может просматривать описания произведений, читать отзывы и комментарии
2. Аутентифицированный пользователь — может выполнять все те же действия что и аноним, может публиковать отзывы и ставить оценки произведениям, может комментировать отзывы, редактировать или удалять свои отзывы и комментарии, редактировать свои оценки произведений. Просматривать свою учётную запись и редактировать её. Эта роль присваивается по умолчанию каждому новому пользователю.
3. Модератор — те же права, что и у аутентифицированного пользователя, плюс право удалять и редактировать любые отзывы и комментарии.
4. Администратор — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.
5. Суперюзер — всегда обладает правами администратора. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора.

## Регистрация пользователей
### Самостоятельная регистрация
1. Пользователь отправляет Post запрос с параметрами ```email``` и  ```username``` на эндпоинт ```/api/v1/auth/signup/```
2. Сервис YaMDB отправляет письмо с кодом подтверждения (confirmation_code) на указанный адрес email.
3. Пользователь отправляет Post запрос с параметрами ```username``` и ```confirmation_code``` на эндпоинт ```/api/v1/auth/token/```, в ответе на запрос ему приходит токен
### Создание пользвотеля администратором
Пользователя может создать администратор — через админ-зону сайта или через Post запрос на специальный эндпоинт ```api/v1/users/``` (описание полей запроса для этого случая — в документации). В этот момент письмо с кодом подтверждения пользователю отправлять не нужно. После этого пользователь должен сделать те же действия что и при самостоятельной регистрации.

# Подготовка к запуску и запуск проекта api_yamdb

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в основную папку и выполнить миграции:

```
cd api_yamdb
```

Выполнить миграцию:

```
python manage.py migrate
```

Заполненить базу данных CSV-файлами:

```
python manage.py uploadDB users.csv category.csv genre.csv titles.csv review.csv comments.csv
```

Запустить проект:

```
python manage.py runserver
```

# Документация к API
Документация к API доступна после запуска проекта по ссылке:
http://127.0.0.1/redoc/

# Используемые технологии
- Python
- Django REST framework
- Git
- SQLite3
- Simple JWT

# Разработчики

[Скалозубов Максим](https://github.com/mmjax): управление пользователями (Auth и Users): система регистрации и аутентификации пользователей, пользовательские роли и права доступа, работа с токеном, система подтверждения через e-mail.

[Трохимец Константин](https://github.com/Trohimets): категории (Categories), жанры (Genres) и произведения (Titles): модели, view и эндпойнты. Рейтинги произведений.

[Дорошенко Виктор](https://github.com/Dorosh93): отзывы (Review) и комментарии (Comments): модели, view и эндпойнты.
