from django.urls import path
from .views import(
     CreateClientView,HomeView, RtnDeviceDetail, RtnDeviceView,SearchResultView, 
     UpdateClientView,DeleteClientView,DetailClientView
)

app_name = 'crm'

urlpatterns = [
    path('',HomeView.as_view(),name='index'),
    path('search/',SearchResultView.as_view(),name='search'),
    path('client/create/',CreateClientView.as_view(),name='create-client'),
    path('<int:pk>/detail/',DetailClientView.as_view(),name='detail-client'),
    path('<int:pk>/update/',UpdateClientView.as_view(),name='update-client'),
    path('<int:pk>/delete/',DeleteClientView.as_view(),name='delete-client'),
    
    path('returned_device',RtnDeviceView.as_view(),name='returned-device'),
    path('<int:pk>/returned_device_detail/',RtnDeviceDetail.as_view(),name='detail-returned-device'),    
    
]