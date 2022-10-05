from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from ProyectoWT.views import bucketList, home, integrantes
from Acceso.views import login_request, register,  agregar_avatar, ProfileUpdateView, Logout, editar_avatar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proyecto-WT/', include('AppWT.urls')),
    #Registro usuario y sesion
    path('login/', login_request, name = 'login'),
    # path('login/', views.CustomLoginView.as_view, name = 'login'),
    path('login/register/', register, name = 'register'),
    path('logout/', Logout.as_view(), name='logout'),
    # URLS Perfil
    path('editar-perfil/', ProfileUpdateView.as_view(), name="editar_perfil"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
    path('editar-avatar/', editar_avatar, name="editar_avatar"),
    #Pestaña Principal
    path('', home, name="home"),

    path('bucketList/', bucketList, name="bucketList"),
    #About US
    path('about-us/', integrantes , name="about_us"),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

