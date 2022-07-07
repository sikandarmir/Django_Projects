
from django.contrib import admin
from django.urls import path

from enroll import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.UserAddshowView.as_view(), name='addandshow'),
    # path('', views.add_show, name='addandshow'),
    path('delete/<int:id>/', views.UserDeleteView.as_view(), name='delete_data'),
    path('<int:id>/', views.UserupdateView.as_view(), name='update_data'),
    



]
