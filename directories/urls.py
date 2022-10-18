from django.urls import path
from .views import GetDirContent

urlpatterns = [
    path('', GetDirContent.as_view())
]
