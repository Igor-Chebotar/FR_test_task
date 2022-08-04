from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet

from .models import Tag, Client, Distribution, Message
from .serializers import TagSerializer, ClientSerializer, DistributionSerializer, MessageSerializer


class TagViewsSet(ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['id']


class ClientViewsSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['tag', 'operator_code']


class DistributionViewsSet(ModelViewSet):
    queryset = Distribution.objects.all()
    serializer_class = DistributionSerializer


class MessageViewsSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MainView(TemplateView):
    template_name = 'mailer_main.html'
