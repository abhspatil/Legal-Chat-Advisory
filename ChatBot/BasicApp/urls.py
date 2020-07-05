from django.urls import path

from . import views

urlpatterns = [
    path('setData', views.setData, name='setData'),
    path('getData', views.getData, name='getData'),
    path('uploadData',views.uploadData,name='uploadData'),
    path('submitData',views.submitData,name='submitData'),
    path('home',views.home,name="home"),
    path('tojson',views.toJson,name='tojson'),
    path('mlapi',views.mlAPI,name='mlAPI'),
    path('querysubmit',views.QueryDataSubmit,name='submitQueryData'),
    
]