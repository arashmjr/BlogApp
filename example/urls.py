from django.urls import path
from example.views import RegisterView, LoginView, CreateTokens
from django.conf.urls import include

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('api-token-auth/', CreateTokens.as_view()),
    path('', include('post.urls')),

]
