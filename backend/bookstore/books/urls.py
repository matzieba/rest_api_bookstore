from django.urls import path
from . import views


urlpatterns = [
    path('', views.book_create_view),
    path('list', views.book_list_view),
    # path('<int:pk>/', views.book_detail_view),
    path('<int:pk>/update/', views.book_update_view),
    path('<int:pk>/delete/', views.book_destroy_view),
]
