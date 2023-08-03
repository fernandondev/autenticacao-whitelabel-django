from allauth.account.views import SignupView, LoginView
from django import forms
from django.contrib import messages
import tldextract
from .models import Unidade, Usuario
from django.shortcuts import render
from .forms import UsuarioUpdateForm
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.http import QueryDict

#Monta tela inicial dos dados do usuário
def pagina_inicial(request):

    usuario = request.user
    return render(request, 'usuarios/usuarios.detalhe.html', {'usuario' : usuario})


#edita o usuário logado. Se for get, renderiza a view de editar
#Se for post e o form for válido, atualiza o usuário
#Se for post e o form for inválido, renderiza a view editar com os erros
#O usuário é sempre pegado a partir do backend e não de acordo com o id passado pela path, para evitar fraudes
def editar_usuario_logado_pagina(request):

    if request.method == 'GET':
        form = UsuarioUpdateForm()
        usuario = request.user
        return render(request, 'usuarios/usuarios.editar.html', {'form': form, 'usuario': usuario})
    else:
        form = UsuarioUpdateForm(request.POST)
        usuario = request.user
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            #Bloqueia que o email escolhido seja igual à um email já existente
            lista_usuarios_com_esse_email = Usuario.objects.filter(email=email)
            if lista_usuarios_com_esse_email.count() > 0 and usuario.email != email:
                usuario = Usuario()
                usuario.email = form.cleaned_data['email']
                usuario.first_name = form.cleaned_data['first_name']

                return render(request, 'usuarios/usuarios.editar.html', {'form': form, 'usuario': usuario, 'email_cadastrado': True})

            #Preenche e salva o usuário
            usuario.email = email
            usuario.set_password(password)
            usuario.first_name = first_name
            usuario.save()
            #Força logout
            logout(request)
            #Deleta as messages
            storage = messages.get_messages(request)
            storage.used = True

            messages.add_message(request, messages.WARNING, "O usuário foi atualizado. Faça login novamente!")

            return redirect('/')
        else:
            usuario = Usuario()
            usuario.email = form.cleaned_data['email']
            usuario.first_name = form.cleaned_data['first_name']

            return render(request, 'usuarios/usuarios.editar.html', {'form': form, 'usuario': usuario})

#Pega o usuário da requisição, deleta e faz logout
#Ao tentar redirecionar para '/', que precisa de
#login, redirecionará para a tela de login.
def deletar_usuario_logado(request):

    usuario = request.user
    usuario.delete()
    logout(request)
    # Deleta as messages
    storage = messages.get_messages(request)
    storage.used = True
    messages.add_message(request, messages.WARNING, "O usuário foi deletado. Para logar, cadastre-se novamente!")

    return redirect('/')

# Sobrescreve a SignupView do AllAuth, para receber o suporte
# para autenticação por unidade
class UsuarioSignUpView(SignupView):

    #Sobrescrevendo o método form_valid da classe SignupView
    #Redirecionando para a tela de login, se o formulário UsuarioSignUpForm
    #lançar a exceção ValidationError
    def form_valid(self, form):
        try:
            #chama o método get_context_data da classe UsuarioSignUpView original 
            return super(UsuarioSignUpView, self).form_valid(form)
        except forms.ValidationError as e:
            messages.add_message(self.request, messages.WARNING, "Não há unidade para essa url informada")
            self.request.POST = QueryDict()
            return UsuarioSignUpView.as_view()(self.request)


    #Sobrescrevendo o método de carregamento do template
    #Se a url não mapear nenhuma unidade, retorna erro 500
    def render_to_response(self, context, **response_kwargs):

        #Extrai o nome da unidade do subdomínio
        nome_unidade = tldextract.extract(self.request.build_absolute_uri()).subdomain
        # Vai lançar exceção se não achar unidade a partir do subdominio passado
        unidade = Unidade.objects.get(nome=nome_unidade)

        response_kwargs.setdefault("content_type", self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs,
        )

        # Adiciona a url_imagem à view

    #Sobrescrevendo o método get_context_data da classe SignupView
    def get_context_data(self, **kwargs):

        #Extrai o nome da unidade do subdomínio
        nome_unidade = tldextract.extract(self.request.build_absolute_uri()).subdomain

        # Vai lançar exceção se não achar unidade a partir do subdominio passado
        unidade = Unidade.objects.get(nome=nome_unidade)

        #chama o método get_context_data da classe SignupView original 
        context = super(UsuarioSignUpView, self).get_context_data(**kwargs)
        context['url_imagem'] = unidade.url_imagem

        return context
    
#Sobrescreve a LoginView do AllAuth, para receber o suporte
#para autenticação por unidade
class UsuarioLoginView(LoginView):

    #Sobrescrevendo o método form_valid da classe LoginView
    #Redirecionando para a tela de login, se o formulário UsuarioLoginForm lançar a exceção ValidationError
    def form_valid(self, form):
        try:
            #chama o método form_valid da classe LoginView original 
            return super(UsuarioLoginView, self).form_valid(form)
        except forms.ValidationError as e:
            messages.add_message(self.request, messages.WARNING, "O usuário não possui conta nessa unidade")
            print(self.request)
            self.request.POST = QueryDict()
            return UsuarioLoginView.as_view()(self.request)

    #Sobrescrevendo o método render_to_response da classe LoginView
    #Esse método é o que realiza o carregamento do template.
    #Se a url não mapear nenhuma unidade, retorna erro 500
    def render_to_response(self, context, **response_kwargs):

        #Extrai o nome da unidade do subdomínio
        nome_unidade = tldextract.extract(self.request.build_absolute_uri()).subdomain

        #Vai lançar exceção se não achar unidade a partir do subdominio passado
        unidade = Unidade.objects.get(nome=nome_unidade)
        print(type(self.request.POST))
        response_kwargs.setdefault("content_type", self.content_type)
        return self.response_class(
            request=self.request,
            template=self.get_template_names(),
            context=context,
            using=self.template_engine,
            **response_kwargs,
        )
    
    #Sobrescrevendo o método get_context_data da classe LoginView
    #Adiciona a url_imagem (propriedade da model Unidade) à view
    #Isso permitirá a renderização da imagem da unidade na tela de login
    #De acordo com a unidade extraída do subdomínio
    def get_context_data(self, **kwargs):

        #Extrai o nome da unidade do subdomínio
        nome_unidade = tldextract.extract(self.request.build_absolute_uri()).subdomain
        # Vai lançar exceção se não achar unidade a partir do subdominio passado
        unidade = Unidade.objects.get(nome=nome_unidade)

        #chama o método get_context_data da classe LoginView original 
        context = super(UsuarioLoginView, self).get_context_data(**kwargs)
        context['url_imagem'] = unidade.url_imagem

        return context
