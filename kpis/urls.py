from django.urls import path
from. import views

urlpatterns = [
	path('', views.landing_page, name = 'landing_page'),
	path('accounts/signup/', views.signup, name = 'signup'),
	path('kpis/', views.index, name = 'index'),
	path('kpis/<int:pk>/log_activity/', views.log_activity, name = 'log_activity'),
	path('kpis/<int:pk>/detail', views.kpi_detail, name = 'kpi_detail'),
	path('kpis/<int:pk>/edit/', views.kpi_edit, name = 'kpi_edit'),
	path('kpis/kpi_new/', views.kpi_new, name = 'kpi_new'),
	path('kpis/<int:pk>/detail/<int:pk_act>/delete', views.activity_delete, name = 'activity_delete'),
	path('kpis/<int:pk>/detail/<int:pk_act>/edit', views.activity_edit, name = 'activity_edit'),
	path('kpis/exportCSV', views.export_csv, name = 'export_csv'),

]