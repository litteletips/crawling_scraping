from django.contrib import admin
from django.urls import path, include

from . import views


app_name = 'django_project'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
#    path('login/', views.InquiryView.as_view(), name="login"),
#    path('diary-list/', views.DiaryListView.as_view(), name="diary_list"),
#    path('diary-detail/<int:pk>/', views.DiaryDetailView.as_view(), name="diary_detail"),
#    path('diary-create/', views.DiaryCreateView.as_view(), name="diary_create"),
#    path('diary-update/<int:pk>/', views.DiaryUpdateView.as_view(), name="diary_update"),
#    path('diary-delete/<int:pk>/', views.DiaryDeleteView.as_view(), name="diary_delete"),
#    path('admin/', admin.site.urls),
#    path('', include('diary.urls')),
    path('accounts/', include('allauth.urls')),
]
