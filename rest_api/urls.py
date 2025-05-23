"""
URL configuration for rest_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include, re_path
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions
from graphql_jwt.middleware import JSONWebTokenMiddleware

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from graphene_django.views import GraphQLView


schema_view = get_schema_view(
    openapi.Info(
        title="REST API Documentation using Django Framework",
        default_version='v1',
        description="Comprehensive API documentation providing details on available endpoints and their usage.",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/root/', admin.site.urls),

    # Authentication
    path('api/v1/', include('auth_app.urls')),
    
    # Charivol
    path('api/v1/', include('charivol.urls')),
    
    path(
        "graphql/",
        csrf_exempt(GraphQLView.as_view(
            graphiql=True,
            middleware=[JSONWebTokenMiddleware()],
        )),
    ),

    # Swagger UI and Redoc
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('', lambda request: JsonResponse({"message": "Hi There, this REST API created on Django! "}), name='home'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)