from . import views
from django.urls import path

urlpatterns = [
    path('',views.error_handler_404, name="error"),
    path('',views.error_500, name="error"),
]