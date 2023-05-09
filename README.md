# Тестовое задание на должность Python разработчика 

## Технололгии

### Backend
* [Django](https://www.djangoproject.com/)
* [DRF](https://www.django-rest-framework.org/)
* [Celery](https://docs.celeryq.dev/en/stable/)
* [Redis](https://redis.io/)


## Приложение развернуто [здесь](https://nsign-test-task.onrender.com/) 

### Основное ТЗ выполнено. Дополнительные реализовано

1. Код покрыт юнит тестами

![Landing page](https://raw.githubusercontent.com/aboronilov/fasol-test-task/main/static/img/tests.png)

2. Документация по использованию API

3. Подготовлена статистика по рассылкам на endpoint **** - при переходе на неё на указанный в настройках email отправляется статистика по отправкам

![Landing page](https://raw.githubusercontent.com/aboronilov/fasol-test-task/main/static/img/email.png)

4. Результаты рассылки логируются

5. Если внешний сервер рассылки не отвечает по каким-либо причинам, эта ошибка обработается и рассылка не будет прервана