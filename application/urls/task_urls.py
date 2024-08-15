from django.urls import path
from application.controllers.create_task import CreateTaskAPIView
from application.controllers.get_all_task import GetAllTaskAPIView

urlpatterns = [
    path('create/', CreateTaskAPIView.as_view(), name='create_task_api'),
    path('get-all/', GetAllTaskAPIView.as_view(), name='get_all_task_api')
]
