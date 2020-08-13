from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('tarrifs', views.tarrifsPage, name='tarrifs'),
    path('course/<slug:slug>', views.CourseDetailPage.as_view(), name='course-detail'),
    path('course/<slug:slug>/<slug:lesson_slug>', views.LessonDetailPage.as_view(), name='lesson-detail'),
    path('add-course', views.CourseAddPage.as_view(), name='add-course'),
]