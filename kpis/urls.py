from django.urls import path
from. import views

urlpatterns = [
	path('', views.landing_page, name = 'landing_page'),
	path('kpis/', views.index, name = 'index'),
	path('kpis/<int:pk>/log_activity', views.log_activity, name = 'log_activity'),
	path('kpis/<int:pk>/detail', views.detail, name = 'detail'),

]