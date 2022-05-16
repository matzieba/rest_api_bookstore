from django.urls import path
from . import views


urlpatterns = [
    path('create', views.book_create_view),
    path('', views.book_list_view),
    path('<int:pk>', views.product_mixin_view),
    path('import', views.book_import_view),
]
