from rest_framework import routers
from .views import CSVViewset

csv_router = routers.SimpleRouter()
csv_router.register(r'csv', CSVViewset)


urlpatterns = [

] + csv_router.urls
