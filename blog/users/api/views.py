from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User
from rest_framework import status

class RegisterView(APIView):
    def post(self, request):
        print("registrando usuario...")
        return Response(status=status.HTTP_200_OK, data="TODO OK")