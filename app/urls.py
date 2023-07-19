from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name ='home'),
    path('companies/', Companies.as_view(), name ='companies'),
    path('login/', Login.as_view(), name ='login'),
    path('recurments/', Recurments.as_view(), name ='recurments'),
    path('searchjobs/', Searchjob.as_view(), name ='searchjobs'),
    path('services/', Services.as_view(), name ='services'),
    
]
