
from django.urls import path

from tasks.views import index, index_delete

urlpatterns = [
    path('tasks/', index),
    path('tasks/delete/<int:id>/', index_delete, name='delete'),
]
