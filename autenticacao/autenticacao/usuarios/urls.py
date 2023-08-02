from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    #View de detalhamento do usuário logado
    path('', login_required(views.pagina_inicial), name='listar'),

    #View de edição do usuário logado
    path('editar/', login_required(views.editar_usuario_logado_pagina), name='editar'),

    #View para deletar o usuário logado
    path('deletar/', login_required(views.deletar_usuario_logado), name='deletar'),

    #Realiza cadastro
    # Sobrescreve a SignupView da dependência django-allauth
    path("accounts/signup/", views.UsuarioSignUpView.as_view()),

    #Realiza login
    # Sobrescreve a LoginView da dependência django-allauth
    path("accounts/login/", views.UsuarioLoginView.as_view()),

    #Carrega todas as paths do allauth para autenticação
    path("accounts/", include("allauth.urls")),
    
]
