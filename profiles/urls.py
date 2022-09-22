from django.urls import path
                                                                            
from . import views
    
urlpatterns = [                                  
    path("new/", views.getNewProfls, name="get_new_profiles"),
    path("feed/", views.feed, name="feed"),                              
    path("leadboard/", views.leadboard, name="leadboard"),
    path("<str:username>/", views.getProfile, name="get_user"),
]
