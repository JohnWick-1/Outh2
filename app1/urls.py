from rest_framework import routers
from .views import *
from .serializers import StudentSerializer

router = routers.SimpleRouter()
router.register(r'student', StudentViewSet)

urlpatterns = router.urls
