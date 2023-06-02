from django.urls import path
from users_app.views import UsersListApiView, UserInfoApiView

urlpatterns = [
    path('list/', UsersListApiView.as_view()),
    path('<int:pk>/', UserInfoApiView.as_view()),
]