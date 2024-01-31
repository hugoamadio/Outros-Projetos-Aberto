from django.shortcuts import render
from .models import usuario

def home(request):
    return render(request, "usuarios/home.html")

def cadastro_usuario(request):
    if request.method == 'POST':
        # Salvar dados
        novo_usuario = usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.email = request.POST.get('email')
        novo_usuario.cpf = request.POST.get('cpf')
        novo_usuario.endereco = request.POST.get("endereco")
        novo_usuario.cep = request.POST.get('cep')
        novo_usuario.cidade = request.POST.get('cidade')
        novo_usuario.estado = request.POST.get('estado')
        novo_usuario.save()

    # Exibir usuários cadastrados em uma nova página
    usuarios_cadastrados = usuario.objects.all()

    return render(request, 'app_cadastro_usuario/usuarios.html', {'usuarios': usuarios_cadastrados})


