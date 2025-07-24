from django.urls import path
from .views import Snippet


urlpatterns = [
    path('snippets/', Snippet.as_view({'post': 'create'}), name='snippet'),
]