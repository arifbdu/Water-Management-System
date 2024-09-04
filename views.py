from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import get_user_model
from .models import PondData
from .serializers import PondDataSerializer, UserSerializer

CustomUser = get_user_model()

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class PondDataListCreateView(generics.ListCreateAPIView):
    serializer_class = PondDataSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return PondData.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PondDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PondData.objects.all()
    serializer_class = PondDataSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserTokenObtainPairView(TokenObtainPairView):
    pass

class UserTokenRefreshView(TokenRefreshView):
    pass
