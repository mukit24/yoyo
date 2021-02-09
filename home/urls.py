from django.urls import path,include
from .views import home_view,intermediate_profile,create_volunteer_profile,create_contributer_profile,profile,update_volunteer_profile,update_contributer_profile,profile_view,point_table,contributer_table,about
urlpatterns = [
    path('',home_view,name='home_view'),
    path('im_profile/',intermediate_profile,name='im_profile'),
    path('create_v_profile/<int:id>/',create_volunteer_profile,name='create_v_profile'),
    path('create_c_profile/<int:id>/',create_contributer_profile,name='create_c_profile'),
    path('profile/<int:id>/',profile,name='profile'),
    path('profile_view/<int:id>/',profile_view,name='profile_view'),
    path('update_v_profile/<int:id>/',update_volunteer_profile,name='update_v_profile'),
    path('update_c_profile/<int:id>/',update_contributer_profile,name='update_c_profile'),
    path('point_table/',point_table,name='point_table'),
    path('contributers/',contributer_table,name='con_table'),
    path('about/',about,name='about'),
]