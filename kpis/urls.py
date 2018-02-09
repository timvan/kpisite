from django.urls import path
from. import views

urlpatterns = [
	path('', views.landing_page, name = 'landing_page'),
	path('accounts/signup/', views.signup, name = 'signup'),
	path('kpis/', views.index, name = 'index'),
	path('kpis/kpi_new/', views.kpi_new, name = 'kpi_new'),
	path('kpis/create_examples', views.create_examples, name = 'create_examples'),
	path('kpis/exportCSV', views.export_csv, name = 'export_csv'),
	path('kpis/<int:pk>/log_activity/', views.log_activity, name = 'log_activity'),
	path('kpis/<int:pk>/detail', views.kpi_detail, name = 'kpi_detail'),
	path('kpis/<int:pk>/delete/', views.kpi_delete, name = 'kpi_delete'),
	path('kpis/<int:pk>/edit/', views.kpi_edit, name = 'kpi_edit'),
	path('kpis/<int:pk>/charts/', views.kpi_charts, name = 'kpi_charts'),
	path('kpis/<int:pk>/charts/data', views.ChartData.as_view(), name = 'ChartData'),
	path('kpis/<int:pk>/charts/activity_history', views.ChartHistory.as_view(), name = 'ChartHistory'),
	path('kpis/<int:pk>/datatable/<int:pk_act>/delete', views.activity_delete, name = 'activity_delete'),
	path('kpis/<int:pk>/datatable/<int:pk_act>/edit', views.activity_edit, name = 'activity_edit'),
	path('kpis/<int:pk>/datatable/', views.kpi_datatable, name = 'kpi_datatable'),


]

# path('kpis/<int:pk>/detail/datatable', views.DataTable.as_view(), name = 'DataTable'),