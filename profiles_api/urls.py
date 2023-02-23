from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewset, base_name='hello-viewset')
router.register('profile', views.UserProfilesViewSet)
router.register('feed', views.UserProfileFeedViewSet) #after registering we added permissions in permission.py

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path("", include(router.urls)) 
]