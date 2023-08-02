from allauth.account.forms import LoginForm, SignupForm
from django.utils.translation import gettext_lazy as _
import tldextract
from .models import Unidade, Usuario
from django import forms

#Formulário de atualização do usuário
class UsuarioUpdateForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super(UsuarioUpdateForm, self).clean()

        return cleaned_data

    class Meta:
        model = Usuario
        fields = ["email", "password", "first_name"]
        error_messages = {
            'email': {
                'required': _("O email é obrigatório"),
                'unique': _("Esse email já existe. Escolha um diferente")
            },
            'password': {
                'required': _("A senha é obrigatória")
            }
        }


#Sobrescrição da classe LoginForm da dependência 'allauth'
#para alteração do comportamento do login, com o objetivo
#de só permitir login de um usuário de acordo com a unidade
#ao qual pertence. Esse dado é extraído do subdomínio atual
class UsuarioLoginForm(LoginForm):

    #Tradução das mensagens de validação para português
    error_messages = {
        "account_inactive": _("Conta inativa"),
        "email_password_mismatch": _(
            "Email e senha incorretos"
        ),
        "username_password_mismatch": _(
            "Usuário e/ou senha incorretos."
        ),
        "too_many_login_attempts": _(
            "Muitas tentativas de login."
        ),
    }

    #Efetivação do login de acordo com a unidade do subdomínio
    def login(self, *args, **kwargs):

        #Pega o nome da unidade a partir do subdomínio da url
        nome_unidade = tldextract.extract(self.request.build_absolute_uri()).subdomain

        unidade = Unidade.objects.get(nome=nome_unidade)

        #Verifica se existe um usuário cadastrado na unidade do subdomínio passado
        existe_usuario_para_unidade_do_subdominio = Usuario.objects.filter(unidade=unidade).filter(email=self.request.POST.get('login')).exists()

        #Se não existe um usuário cadastrado na unidade obtida a partir do subdomínio, interrompe login
        if not existe_usuario_para_unidade_do_subdominio:
            raise forms.ValidationError("O usuário não está cadastrado nessa unidade. Favor verificar url")
        abc = super(UsuarioLoginForm, self).login(*args, **kwargs)

        return abc


#Sobrescrição da classe SignupForm da dependência 'allauth'
#para alteração do comportamento do cadastro, com o objetivo
#de definir a unidade do usuário, a partir do subdomínio passado
class UsuarioSignupForm(SignupForm):

    def save(self, request):
        user = super(UsuarioSignupForm, self).save(request)
        nome_unidade = tldextract.extract(request.build_absolute_uri()).subdomain
        try:
            unidade = Unidade.objects.get(nome=nome_unidade)
            user.unidade = unidade
            user.save()
        except Unidade.DoesNotExist:
            unidade = None
            user.delete()
            raise forms.ValidationError("Não existe unidade para a url informada")

        return user
