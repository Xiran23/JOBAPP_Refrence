from django.urls import path 
from app.views import *


urlpatterns = [
    path('',jobs_list,name='jobs_home'),
    path('job/<int:id>',jobs_detail, name ='jobs_detail' ),
    path('hello/' , hello,name = "hello")
    # path('', hello),

]