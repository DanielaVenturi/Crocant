from django.contrib import admin
from django.urls import include, path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from uploader.router import router as uploader_router

from core.views import UserViewSet, ProdutoViewSet, CategoriaViewSet, EstadoViewSet, CidadeViewSet, EnderecoViewSet, PedidoViewSet

router = DefaultRouter()

router.register(r"usuarios", UserViewSet, basename="usuarios")
router.register(r"produtos", ProdutoViewSet, basename="produtos")
router.register(r"categorias", CategoriaViewSet, basename="categorias")
router.register(r"estados", EstadoViewSet, basename="estados")
router.register(r"cidades", CidadeViewSet, basename="cidades")
router.register(r"enderecos", EnderecoViewSet, basename="enderecos")
router.register(r"pedidos", PedidoViewSet, basename="pedidos")

urlpatterns = [
    path("admin/", admin.site.urls),
    # OpenAPI 3
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
        path("api/media/", include(uploader_router.urls)),
    # Simple JWT
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    # API
    path("api/", include(router.urls)),
]
# urlpatterns += static(settings.MEDIA_ENDPOINT, document_root=settings.MEDIA_ROOT)
