"""
URL configuration for shopify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404, handler500
from error.views import error_handler_404, error_500 # ilk once error yaratdiqmiz startapp error-u yazilmali 

handler404 = error_handler_404
handler500 = error_500


urlpatterns = [
    path('elcinadmin/', admin.site.urls), # Admin
    path('product/',include("product.urls")), # Product
    path(r'*',include("error.urls")), # " "
    # path(r'',include("error.urls")) # " "

]
