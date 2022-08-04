from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from taggit.models import TagBase, GenericTaggedItemBase
from timezone_field import TimeZoneField
from taggit.managers import TaggableManager


class Tag(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Client(models.Model):
    # номер телефона клиента в формате 7XXXXXXXXXX (X - цифра от 0 до 9)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    operator_code = models.IntegerField(verbose_name='Код оператора')
    # тег (произвольная метка)
    tag = models.ManyToManyField(Tag)
    # часовой пояс
    time_zone = TimeZoneField(choices_display="WITH_GMT_OFFSET")


class Distribution(models.Model):
    datetime_start = models.DateTimeField()
    mes_text = models.TextField(verbose_name='Текст сообщения')
    # фильтр свойств клиентов, на которых должна быть произведена рассылка
    # (код мобильного оператора, тег)
    operator_code = models.IntegerField(verbose_name='Код оператора')
    tag = models.ManyToManyField(Tag)
    datetime_finish = models.DateTimeField()


class Message(models.Model):
    datetime = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Время отправки')
    sent = models.BooleanField(default=False)
    distribution_id = models.ForeignKey(Distribution, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)