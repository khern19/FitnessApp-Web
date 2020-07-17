from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from users.models import User

# Register API


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Login API


# get UserAPI


# User Viewset
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    serializer_class = UserSerializer
