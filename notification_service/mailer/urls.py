from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import TagViewsSet, ClientViewsSet, DistributionViewsSet, MessageViewsSet, \
    DistributionGetMessagesView

router = SimpleRouter()

router.register(r"tags", TagViewsSet)

router.register(r"clients", ClientViewsSet)

router.register(r"distributions", DistributionViewsSet)

router.register(r"messages", MessageViewsSet)


urlpatterns = [
    path('distributions/<int:pk>/messages', DistributionGetMessagesView.as_view()),
]

urlpatterns += router.urls
