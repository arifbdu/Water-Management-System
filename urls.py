from django.urls import path
from .views import UserRegistrationView, PondDataListCreateView, PondDataDetailView, UserTokenObtainPairView, UserTokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
    path('data/', PondDataListCreateView.as_view(), name='pond-data-list-create'),
    path('data/<int:pk>/', PondDataDetailView.as_view(), name='pond-data-detail'),
    path('token/', UserTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', UserTokenRefreshView.as_view(), name='token_refresh'),
]
