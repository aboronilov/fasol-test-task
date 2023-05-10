# Тестовое задание на должность Python разработчика 

## Технололгии

### Backend
* [Django](https://www.djangoproject.com/)
* [DRF](https://www.django-rest-framework.org/)
* [Celery](https://docs.celeryq.dev/en/stable/)
* [Redis](https://redis.io/)


## Приложение развернуто [здесь](https://fasol-test.onrender.com/api/) 

При добавлении новых сущностей в таблицу Mailer автоматически создаются новые сущности таблицы Message, которые фильтруют клиентов по указанным критериям. Если текущее время попадатает в интервал рассылки - она происходит немедленно. В противном случае - делается отсрочка до начала рассылки

![Landing page](https://raw.githubusercontent.com/aboronilov/fasol-test-task/main/static/img/celery.png)

Для проверки функионала необходимо клонировать репозиторий, создать и активировать окружение, установить зависимости

```git clone https://github.com/aboronilov/fasol-test-task/
cd ./fasol-test-task
python -m venv venv
pip install -r requirements.txt
touch .env```

Так как брокер сообщений Redis уже развернут, предлагаю вставить в файл .env строку:
```CELERY_BROKER_URL=redis://default:uEfcRwZLZCtBNbTECANL@containers-us-west-2.railway.app:6262```

Запустить celery и flower
```cd ..
celery -A notification worker -l info```

### Основное ТЗ выполнено. Дополнительно реализован функционал:

1. Код покрыт юнит тестами 

![Landing page](https://raw.githubusercontent.com/aboronilov/fasol-test-task/main/static/img/tests.png)

2. Документация по использованию API [swagger](https://fasol-test.onrender.com/swagger/) или [redoc](https://fasol-test.onrender.com/redoc/)

3. Подготовлена статистика по рассылкам на endpoint **/message/stat/** - при переходе на него на указанный в .env email дублируется статистика по отправкам

![Landing page](https://raw.githubusercontent.com/aboronilov/fasol-test-task/main/static/img/email.png)

4. Результаты рассылки логируются

5. Если внешний сервер рассылки не отвечает по каким-либо причинам, эта ошибка обработается и рассылка не будет прервана

6. Деплой приложения (сам сервер, база данных и брокер сообщений)
