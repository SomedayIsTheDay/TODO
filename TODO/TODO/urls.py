"""TODO URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from usersapp.views import TODOUserCustomViewSet
from mainapp.views import ProjectModelViewSet, TODONotesModelViewSet
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

# from graphene_django.views import GraphQLView

schema_view = get_schema_view(
    openapi.Info(
        title="TODO",
        default_version="1.0",
        description="Documentation to TODO API",
        contact=openapi.Contact(email="admin@admin.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

router = DefaultRouter()
router.register("users", TODOUserCustomViewSet)
router.register("projects", ProjectModelViewSet)
router.register("TODO", TODONotesModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/", include(router.urls)),
    path("api-token-auth/", views.obtain_auth_token),
    # path("graphql/", GraphQLView.as_view(graphiql=True)),
    path("", TemplateView.as_view(template_name="index.html")),
    path("swagger<str:format>/", schema_view.without_ui()),  # noqa
    path("swagger/", schema_view.with_ui("swagger")),  # noqa
    # path("redoc/", schema_view.with_ui("redoc")),  # noqa
]
