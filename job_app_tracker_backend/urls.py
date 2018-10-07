from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views import CompanyViewSet, ApplicationViewSet, InterviewViewSet

router = SimpleRouter()
router.register('companies', CompanyViewSet, base_name='company')
router.register('applications', ApplicationViewSet, base_name='application')
router.register('interviews', InterviewViewSet, base_name='interview')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]