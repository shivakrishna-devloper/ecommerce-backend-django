from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

# Router automatically maps URLs to ViewSet actions
router = DefaultRouter()

# This creates endpoint like:
# /products/, /product/{id}/
router.register(r'products', ProductViewSet)

urlpatterns = router.urls