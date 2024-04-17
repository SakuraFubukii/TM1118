from django.urls import path
from . import views
urlpatterns = [

    path('', views.dashboard),
        
    # data
    path('data_event', views.data_events),
    path('dashboard-data', views.data_dashboard, name='dashboard-data'),
    # test
    path('graph/overview', views.graph_overview),
    path('location', views.location),


    path('index', views.index),
    path('show/B05', views.showB05),
    path('test', views.test),
   
    
    path('data_test', views.data_test),
    path('data_test2', views.data_test2),
   
    path('data_dA01', views.data_dashboardA01),

]