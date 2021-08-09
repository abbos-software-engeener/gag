from django.urls import path
from .views import ClientRegistration, ClientLogin, client_logout, ClientProfile

app_name = "client"

urlpatterns = [
    path('registration/', ClientRegistration.as_view(), name="registration"),
    path('login/', ClientLogin.as_view(), name="login"),
    path('logout/', client_logout, name="logout"),
    path('profile/', ClientProfile.as_view(), name="profile")

]