from django.shortcuts import render
from django.views.generic import TemplateView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .context_processors import get_messages
from .models import Tag, Client, Distribution, Message
from .serializers import TagSerializer, ClientSerializer, DistributionSerializer, MessageSerializer
from .tasks import distribution_send_function


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        distribution_send_function.delay(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DistributionGetMessagesView(TemplateView):
    template_name = 'distributions_messages.html'

    def get(self, request, pk):
        ctx = get_messages(request)
        return render(request, self.template_name, ctx)


class MessageViewsSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
