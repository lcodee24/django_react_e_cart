from django.urls import path

from . import views

urlpatterns = [
    path('cartproduct/',views.Usercartproduct.as_view()),
    # path('cartshow/',views.Usercartshow.as_view())
]
