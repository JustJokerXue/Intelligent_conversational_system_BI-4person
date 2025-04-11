"""USTD_Dev_all URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from ICS_app import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
# import notifications.urls

app_name = 'ICS_app'

urlpatterns = [
    # 核心功能路由
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path('', views.index, name='index'),
    #
    # # 认证系统路由组
    # path('auth/', include([
    #     path('login/', views.login, name='login'),
    #     path('logout/', views.logout, name='logout'),
    #     path('register/', views.register, name='register'),
    # ])),
    #
    # # 用户个人中心路由组
    # path('profile/', include([
    #     path('edit/', views.profile_edit, name='profile_edit'),
    #     path('update/', views.update_profile, name='update_profile'),
    # ])),
    #
    # # 业务功能路由
    # path('doctor/chat/<str:receiver_account>/', views.doctor_chat, name='doctor_chat'),
    # # path('doctor/chat/<str:doctor_id>/', views.doctor_chat, name='doctor_chat'),
    # path('chat/send/', views.send_message, name='send_message'),
    # path('chat/get/<str:receiver_account>/', views.get_messages, name='get_messages'),
    # # path('chat/get/<str:doctor_id>/', views.get_messages, name='get_messages'),
    # path('doctor/chat/history/<str:doctor_id>/', views.doctor_chat_history, name='doctor_chat_history'),
    # path('doctor/', views.doctor, name='doctor'),
    # path('chat/', views.doctor_chat, name='doctor_chat'),
    # path('ai-doctor/', views.AI_doctor, name='ai_doctor'),
    # path('ai-diagnosis/', views.ai_diagnosis, name='ai_diagnosis'),
    # path('detection_history/', views.detection_history, name='detection_history'),

    # # API端点路由组
    # path('api/', include([
    #     path('profile/', views.update_profile, name='api_update_profile'),
    # ])),
]

# 开发环境静态文件服务配置
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)