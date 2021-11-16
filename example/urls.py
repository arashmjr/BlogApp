from django.urls import path
from example.views import RegisterView, LoginView, CreateTokens
from django.conf.urls import url, include

urlpatterns = [
    url('register/', RegisterView.as_view(), name="register"),
    url('login/', LoginView.as_view(), name="login"),
    path('api-token-auth/', CreateTokens.as_view()),

]
