from django.urls import path,include
from django.conf.urls import url
from Prediction.views import Ulogin,Registration

urlpatterns =[
    path("register/",Registration,name="Register"),
    path("login/",Ulogin,name="Login"),

]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)