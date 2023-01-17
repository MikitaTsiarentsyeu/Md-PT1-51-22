"""FinalProject URL Configuration

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
from django.urls import path, include
from handmade import views as hm_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', hm_views.home, name = "home"),
    path('materials/', hm_views.materials, name = "materials"),
    path('products/', hm_views.products, name = "products"),
    path('accessories/', hm_views.accessories, name="accessories"),
    path('rests/', hm_views.rests, name="rests"),
    path('materials/add_material', hm_views.add_material, name="add_material"),
    path('products/add_product', hm_views.add_product, name="add_product"),
    path('accessories/add_accessory', hm_views.add_accessory, name="add_accessory"),
    path('products/<int:product_id>', hm_views.product, name='product'),
    path('materials/<int:material_id>', hm_views.material, name='material'),
    path('accessories/<int:accessory_id>', hm_views.accessory, name='accessory'),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)