from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import RegistrationSerializer

from django.utils.translation import gettext as _


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        user = serializer.save()
        user.save()

        return Response(
            {"message": _("Registration successful. Please confirm your email.")},
            status=status.HTTP_201_CREATED
        )
