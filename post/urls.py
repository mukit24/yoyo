from django.urls import path,include
from .views import post_view,react,add_comment,post_details,delete_comment,delete_post,edit_comment,react_d
urlpatterns = [
    path('',post_view,name='post_view'),
    path('react/<int:id>/',react,name='react'),
    path('react_d/<int:id>/',react_d,name='react_d'),
    path('posts/<int:id>/comment/',add_comment,name='add_comment'),
    path('posts/<int:id>/details/',post_details,name='post_details'),
    path('posts/<int:id>/delete/',delete_post,name='delete_post'),
    path('comment/<int:id>/edit/',edit_comment,name='edit_comment'),
    path('posts/<int:id>/delete_comment/',delete_comment,name='delete_comment'),
]