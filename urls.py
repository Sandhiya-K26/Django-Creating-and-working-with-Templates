from django.contrib import admin
from django.urls import path
from newapp import views as newapp_views  # Import views from ex2app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', newapp_views.home, name='home'),  # Route for the home page
    path('oddfilter/', newapp_views.oddfilter, name='oddfilter'),  # Route for the odd view
    #path('filter/', newapp_views.filter, name="filter_names"),
    
]
