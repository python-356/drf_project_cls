from django.urls import path, include
from backs import views


urlpatterns = [
    path('cls/list', views.ClassScheduleList.as_view(), name='cls-list'),
    path('cls/detail/<int:pk>', views.ClassScheduleDetail.as_view(), name='cls-detail'),
]