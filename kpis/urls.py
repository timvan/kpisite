from django.urls import path
from. import views

urlpatterns = [
	path('', views.landing_page, name = 'landing_page'),
	path('accounts/signup/', views.signup, name = 'signup'),
	path('kpis/', views.index, name = 'index'),
	path('kpis/<int:pk>/log_activity', views.log_activity, name = 'log_activity'),
	path('kpis/<int:pk>/', views.kpi_detail, name = 'kpi_detail'),
	path('kpis/kpi_new', views.kpi_new, name = 'kpi_new'),

]