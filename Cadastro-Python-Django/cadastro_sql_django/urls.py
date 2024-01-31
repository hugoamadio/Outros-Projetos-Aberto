from django.urls import path
from app_cadastro_usuario import views


urlpatterns = [
    #ROTA -> VIEW RESPONSAVEL - > NOME DE REFERENCIA
    path("",views.home, name="home"),
    path("usuario/", views.cadastro_usuario, name="listagem_usuario")
]
