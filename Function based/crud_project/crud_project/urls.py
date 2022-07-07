
from django.contrib import admin
from django.urls import path

from enroll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_show, name='addandshow'),
    path('delete/<int:id>/', views.delete_data, name='delete_data'),
    path('<int:id>/', views.update_data, name='update_data'),



]
