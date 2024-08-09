from django.urls import path
from django import views
from .views import loading_dataset
urlpatterns = [
   path('dataset',views.loading_dataset,name="loading_dataset")]