from django.urls import path
from rest_framework.routers import DefaultRouter
from api.apiviews import ProductoDetalle, ProductoList, \
    CategoriaList, SubCategoriaList, CategoriaDetalle, \
    SubCategoriaAdd, ProductoViewSet, UserCreate, LoginView
from rest_framework.authtoken import views
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls


router = DefaultRouter()
router.register('v2/productos', ProductoViewSet, base_name='productos')

schema_view = get_swagger_view(title='Rest Full API')

urlpatterns = [
    path('v1/productos/', ProductoList.as_view(), name='producto_list'),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(), name='producto_detalle'),
    path('v1/categorias/', CategoriaList.as_view(), name='categoria_list'),
    # path('v1/subcategorias/', SubCategoriaList.as_view(),name='subcategoria_list' )
    path('v1/categorias/<int:pk>', CategoriaDetalle.as_view(), name='categoria_list'),
    path('v1/categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(), name='sc_list'),
    path('v1/categorias/<int:cat_pk>/addsubcategorias/', SubCategoriaAdd.as_view(), name='sc_add'),
    path('v3/usuarios/', UserCreate.as_view(), name='usuario_crear'),
    path("v4/login/", LoginView.as_view(), name="login"),
    path("v3/login-drf/", views.obtain_auth_token, name="login_drf"),
    path('swagger-docs/', schema_view),
    path('coreapi-docs/', include_docs_urls(title="Rest Api Documentation")),
]

urlpatterns += router.urls





