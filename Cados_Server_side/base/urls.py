from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('',views.endpoints,name='home'),
    path('advocates/',views.advocates_list,name='advocate-list'),
    path('advocates/<str:username>/',views.AdvocateDetail.as_view(),name='advocate-detail'),
    # path('advocates/<str:username>/',views.advocate_detail,name='advocate-detail')

    path('companies/',views.Companies_list,name='companies-list'),
]
