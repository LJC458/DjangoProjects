"""TestMagazineProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path ,re_path #used to be url
from Magazine import views as m_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',m_views.view),
    path('posts/',m_views.PostList),
    path('api/posts/',m_views.PostJson),
    #path('reflect/<int:id>',views.Reflect),
    re_path(r'reflect/(?P<pk>\d+)',m_views.Reflect) #pk=primarykey
]
