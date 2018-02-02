from django.urls import path
from. import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:pk>/log_activity', views.log_activity, name = 'log_activity'),

]