from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('',views.index,name='index.html'),
  path('home',views.indexDemo,name='indexDemo.html'),
  path('about',views.about,name='about.html'),
  path('contact',views.contact,name='contact.html'),
  path('birthday',views.birthday,name='birthday.html'),
  path('blog',views.blog, name="blog.html"),
  path('corporate',views.corporate,name='corporate.html'),
  path('D1',views.D1,name='D1.html'),
  path('success', views.success, name='payment_status'),
  path('payment', views.payment, name="payment.html"),
  path('services',views.services,name='services.html'),
  path('festival',views.festival,name='festival.html'),
  path('portfolio',views.portfolio,name='portfolio.html'),
  path('post',views.post,name='post.html'),
  path('ringceremony',views.ringceremony,name='ringceremony.html'),
  path('profile',views.profile,name='profile.html'),
  path('editprofile',views.editprofile,name='editprofile.html'),
  path('special_page',views.special_page,name='special_page.html'),
  path('wedding/<slug:header>',views.wedding,name='header'),
  path('login',views.login_user, name='login'),
  path('register_user',views.register_user, name='register'),
  path('logout_user',views.logout_user, name='logout'),
  path('profile_user',views.profile_user, name='profile'),
  path('edit_profile_user',views.edit_profile, name='edit_profile_user'),
  path('change_password/', views.change_password, name='change_password'),
  path('thank', views.thank, name='thank.html'),
  path('delete_comment/<int:id>/', views.delete_comment, name='delete_comment'),
 

    # [1] Submit Email Form                             //PasswordResetView.as_view()
    # [2] Email Sent Success Message                    //PasswordResetDoneView.as_view()
    # [3] Link to Password Reset form in Email          //PasswordResetConfirmView.as_view()
    # [4] Password successfullt changed message         //PasswordResetCompleteView.as_view()

    path('reset_password/', 
         auth_views.PasswordResetView.as_view(template_name="password_reset.html"), 
         name="reset_password"),
    path('reset_password_sent/', 
         auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), 
         name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete.html"), 
         name="password_reset_complete"),
]



