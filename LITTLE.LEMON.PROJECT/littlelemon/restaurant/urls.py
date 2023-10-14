#define URL route for index() view
from django.urls import path,include
from . import views

app_name = 'restaurant'
urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view(),name='menu'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]
