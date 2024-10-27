"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from studentWorksPlatform.views import WorkListView, WorkDetailView, WorkCreateView, WorkUpdateView, WorkDeleteView, UserListView, UserAPI, WorkAPI
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()

router.register('usersApi', UserAPI, basename='usersApi')
router.register('worksApi', WorkAPI, basename='worksApi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(), name='swagger'),
    path('', WorkListView.as_view(), name='work_list'),
    path('work/<int:pk>/', WorkDetailView.as_view(), name='work_detail'),
    path('work/create/', WorkCreateView.as_view(), name='add_work'),
    path('work/<int:pk>/edit/', WorkUpdateView.as_view(), name='work_edit'),
    path('work/<int:pk>/delete/', WorkDeleteView.as_view(), name='work_delete'),

    path('users/', UserListView.as_view(), name='user_list'),
]  + router.urls
