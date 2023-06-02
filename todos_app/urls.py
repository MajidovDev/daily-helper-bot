from django.urls import path
from todos_app.views import TodosListApiVeiw, TodosInfoApiView

urlpatterns = [
    path('list/', TodosListApiVeiw.as_view()),
    path('<int:pk>/', TodosInfoApiView.as_view()),
]