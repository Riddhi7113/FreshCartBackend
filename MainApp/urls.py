from django.urls import path
from .views import home, login_view

app_name = 'MainApp'

urlpatterns = [
    
    path('', home, name='home'),
    path('login/', login_view, name='login'),
]
