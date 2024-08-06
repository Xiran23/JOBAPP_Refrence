from .import views
from django.urls import path
urlpatterns = [
     path('images',views.upload_image, name='upload_image'),
     path('file',views.upload_file, name='upload_file')
]
