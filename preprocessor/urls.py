from django.urls import path
from rest_framework import routers
import preprocessor.views as views 


csv_router = routers.SimpleRouter()
csv_router.register(r'preprocessor/csv', views.CSVViewset)


urlpatterns = [
    path('csv/list/', views.get_csv_list),
    path('csv/list/groups/', views.get_date_range),
    path('csv/list/summary/', views.get_job_summary),
] + csv_router.urls

