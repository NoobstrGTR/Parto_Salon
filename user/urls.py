from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('get_user_data/',views.get_user_data),
    path('get_user_data_by_id/<int:id>', views.get_user_data_by_id),
    path('post_user_data/', views.post_user_data),
    path('edit_user_data/', views.edit_user_data),
    path('delete_user_data/<int:id>', views.delete_user_data)
]
