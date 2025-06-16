from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import HasPermission

class MyProtectedView(APIView):
    permission_classes = [IsAuthenticated, HasPermission]
    required_permission = 'view_dashboard'

    def get(self, request):
        return Response({"message": "你有权限访问这个接口"})