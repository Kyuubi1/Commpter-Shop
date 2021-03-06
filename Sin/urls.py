from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
app_name = 'Sin'

urlpatterns = [
    path('', views.ClassIndex.as_view(), name='index'),
    path('login/', views.ClassLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('sign-up/', views.SignupView.as_view(), name='sign-up'),
    path('profile/', views.InforUser.as_view(), name='profile'),
    path('profile/edit/', views.AccountUpdate.as_view(), name='edit-profile'),
    path('service/', views.ServiceView.as_view(), name='service'),
    path('product/detail/<int:product_id>/', views.DetailProduct.as_view(), name='detail'),
    path('service/register', views.RegisterService.as_view(), name='service_register'),
    path('service/complete/', views.SuccessRegister.as_view(), name='success_register'),
    path('service/assignee/', views.ServiceAssignee.as_view(), name='assignee'),
    path('cart/', views.BoxProduct.as_view(), name='cart'),
    path('cart/<int:cart_id>/', views.DeleteProduct.as_view(), name='cart_delete'),
    path('assignee/detail/', views.AssigneeDetail.as_view(), name='assignee_detail'),
    path('report/', views.ReportView.as_view(), name='report'),
    path('payment/', views.Payment.as_view(), name='payment'),
    path('search/', views.Search.as_view(), name='search'),
    path('search/?category="HP"/', views.HP.as_view(), name='search-HP'),
    path('search/?category="MacBook"/', views.Mac.as_view(), name='search-Mac'),
    path('search/?category="Acer"/', views.Acer.as_view(), name='search-Acer'),
    path('search/?category="Asus"/', views.Asus.as_view(), name='search-Asus'),
    path('search/?category="Dell"/', views.Dell.as_view(), name='search-Dell'),
    path('search/?category="MSI-Gaming"/', views.MSI.as_view(), name='search-MSI'),

]