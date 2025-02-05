from rest_framework.routers import DefaultRouter 
from .views import UserViewSet, PostViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = router.urls