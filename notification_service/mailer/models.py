from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Client(models.Model):
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    operator_code = models.IntegerField(null=False, blank=False, verbose_name='Код оператора')
    tag = models.ManyToManyField(Tag)
    time_zone = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Distribution(models.Model):
    datetime_start = models.DateTimeField(null=False, blank=False)
    msg_text = models.TextField(verbose_name='Текст сообщения')
    operator_code = models.IntegerField(verbose_name='Код оператора')
    tag = models.ManyToManyField(Tag)
    datetime_finish = models.DateTimeField(null=False, blank=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Message(models.Model):
    datetime = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Время отправки')
    sent = models.BooleanField(default=None)
    distribution_id = models.ForeignKey("Distribution", on_delete=models.CASCADE)
    client_id = models.ForeignKey("Client", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
