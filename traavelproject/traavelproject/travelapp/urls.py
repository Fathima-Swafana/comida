from . import views
from django.urls import path
app_name='travelapp'
urlpatterns = [

    path('',views.index,name='index'),
    path('comida/<int:comida_id>/',views.detail,name='detail'),
    path('add/',views.add_comida,name='add_comida'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]