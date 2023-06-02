from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from todos_app.models import TodosModel
from todos_app.serializers import TodosSerializer
from users_app.models import UserModel


class TodosListApiVeiw(APIView):
    def get(self, request):
        try:
            # user = self.request.user
            user = UserModel.objects.get(id="1")
            todos_list = TodosModel.objects.filter(creator=user.id)
            serializer = TodosSerializer(todos_list, many=True)
            data = {
                "success": True,
                "message": serializer.data,
                "creater": str(user)
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e))


class TodosInfoApiView(APIView):
    def get(self, request, pk):
        try:
            user = UserModel.objects.get(id="1")
            todos = TodosModel.objects.get(creator=user.id, id=pk)
            serializer = TodosSerializer(todos)
            data = {
                "success": True,
                "message": serializer.data,
                "creater": str(user)
            }
            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e))
