from django.urls import path
from . import views
urlpatterns = [
    path('oddfilter/', views.odd, name='oddfilter'),  # Maps /odd/ URL to the odd view
    path('filter/', views.filter_names, name='filter_names'),  # Maps /filter/ URL to the filter_names view
]
