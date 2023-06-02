from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users_app.serializers import UserSerializer
from users_app.models import UserModel


class UsersListApiView(APIView):
    def get(self, request):
        try:
            users = UserModel.objects.all()
            serializer = UserSerializer(users, many=True).data
            data = {
                "success": True,
                "message": serializer
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e))


class UserInfoApiView(APIView):
    def get(self, request, pk):
        try:
            user = UserModel.objects.get(id=pk)
            serializer = UserSerializer(user).data
            data = {
                "success": True,
                "message": serializer
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e))
