# для API
from tastypie import fields
from tastypie.resources import ModelResource
from riddles.models import Riddle, Option
# для безопасности API
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie.serializers import Serializer


# класс для управления загадками
class RiddleResource(ModelResource):
    # описание
    class Meta:
        # набор данных - все загадки из БД
        queryset = Riddle.objects.all()
        # имя, которое нужно указывать в URL после /api/
        resource_name = 'riddle'
        # требуем указать логин и пароль в заголовках
        authentication = BasicAuthentication()
        # права на добавление-обновление-удаление
        # выдаем на основании логина и пароля - только админам
        authorization = DjangoAuthorization()
        # стандартный класс для сохранения
        serializer = Serializer()


# класс для управления вариантами ответов
class OptionResource(ModelResource):
    # ID загадки, к которой относится вариант ответа
    # (переменной из модели), по умолчанию не выводится
    # из-за того, что это внешний ключ
    riddle_id = fields.IntegerField('riddle_id')
    # описание
    class Meta:
        # набор данных - все пользователи из БД
        queryset = Option.objects.all()
        # имя, которое нужно указывать в URL после /api/
        resource_name = 'option'
        # требуем прохождения авторизации
        authentication = BasicAuthentication()
        # права на добавление-обновление-удаление
        # выдаем на основании логина и пароля – только админам
        authorization = DjangoAuthorization()
        # стандартный класс для сохранения
        serializer = Serializer()

