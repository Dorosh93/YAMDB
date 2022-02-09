## Описание проекта YaMDb
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

## Подготовка к запуску и запуск проекта api_yamdb

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

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

## Документация к API
Документация к API доступна после запуска проекта по ссылке:
http://127.0.0.1/redoc/
