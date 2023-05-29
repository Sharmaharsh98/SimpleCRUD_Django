from django.urls import path
from . import views

urlpatterns = [
    path('order/', views.order_view, name='order'),
    path('details/', views.details_view, name='details'),
    path('update/<int:pk>', views.update_view, name='update'),
    path('delete/<int:pk>', views.delete_view, name='delete')
]