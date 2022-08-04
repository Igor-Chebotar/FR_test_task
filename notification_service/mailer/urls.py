from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import TagViewsSet, MainView, ClientViewsSet, DistributionViewsSet, MessageViewsSet

router = SimpleRouter()

router.register(r"tags", TagViewsSet)
router.register(r"tags/<int:pk>", TagViewsSet)

router.register(r"clients", ClientViewsSet)
router.register(r"clients/<int:pk>", ClientViewsSet)

router.register(r"distributions", DistributionViewsSet)
router.register(r"distributions/<int:pk>", DistributionViewsSet)

router.register(r"messages", MessageViewsSet)
router.register(r"messages/<int:pk>", MessageViewsSet)

urlpatterns = [
    path('', MainView.as_view(), name='home'),
]

urlpatterns += router.urls
