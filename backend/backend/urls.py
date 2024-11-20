from django.contrib import admin
from django.urls import path
from poleras import views  # Importamos las vistas desde la app poleras
from django.contrib.auth import views as auth_views  # Importamos las vistas de login/logout de Django

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para acceder al admin
    path('poleras/', views.lista_poleras, name='lista_poleras'),  # Ruta para la vista de poleras
    path('login/', auth_views.LoginView.as_view(template_name='poleras/login.html'), name='login'),  # Ruta para login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Ruta para logout
]
