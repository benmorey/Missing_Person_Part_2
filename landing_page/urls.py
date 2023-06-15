from django.urls import path
from .views import landingPageView, tableView

urlpatterns = [
    path('', landingPageView),
    path('table/', tableView, name='table')
]
