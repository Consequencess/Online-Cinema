from django.urls import include, path
from rest_framework.routers import DefaultRouter

from applications.movie.views import MovieAPIView

router = DefaultRouter()
router.register('', MovieAPIView)

urlpatterns = router.urls