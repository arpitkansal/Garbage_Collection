"""garbagecollection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import include
from apis import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('garbage/driverpath/<int:driver_id>/', views.fetchPath, name = "fetchPath"),
    path('garbage/reached/<int:driver_id>/at/<int:area_id>/', views.fetchReached),
    path('garbage/alertResident/<str:rid>/', views.alertResident),
    path('accounts/', include('django.contrib.auth.urls')),
    path('allareas/',views.fetchArea),
    path('notify/<str:topic_name>/',views.notifyResidents),
    #path('notify/',views.send_to_topic()),
]
