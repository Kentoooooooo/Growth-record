from django.urls import path

from . import views

app_name = 'shift'

urlpatterns = [
    path('shift_list/', views.ShiftListView.as_view(), name='shift_list'),
]
