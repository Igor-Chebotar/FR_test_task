from django.contrib import admin
from .models import Tag, Client, Distribution, Message


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone_number', 'operator_code', 'time_zone']
    list_filter = ['operator_code', 'tag', 'time_zone']


@admin.register(Distribution)
class DistributionAdmin(admin.ModelAdmin):
    list_display = ['operator_code']
    list_filter = ['operator_code', 'tag', 'datetime_start', 'datetime_finish']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['distribution_id', 'client_id', 'datetime', 'sent']
    list_filter = ['sent', 'distribution_id', 'client_id']

