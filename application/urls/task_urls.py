from django.urls import path
from application.controllers.create_task import CreateTaskAPIView

urlpatterns = [
    path('create/', CreateTaskAPIView.as_view(), name='create_tastk_api')
]
