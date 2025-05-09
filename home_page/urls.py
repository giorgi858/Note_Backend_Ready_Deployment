from django.urls import path
from .views import home_page_veiw

urlpatterns = [
    path('', home_page_veiw, name='home'),
    
]