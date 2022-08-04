from django.contrib import admin
from .models import Tag, Client, Distribution, Message


class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag


class ClientAdmin(admin.ModelAdmin):
    class Meta:
        model = Client


class DistributionAdmin(admin.ModelAdmin):
    class Meta:
        model = Distribution


class MessageAdmin(admin.ModelAdmin):
    class Meta:
        model = Message


admin.site.register(Tag, TagAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Distribution, DistributionAdmin)
admin.site.register(Message, MessageAdmin)
