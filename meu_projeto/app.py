from flask import Flask, render_template, request, redirect, url_for
from models import UsuarioModel # Importa o nosso Modelo


app=Flask (__name__)
usuario_model = UsuarioModel() #Instancia o Modelo

@app.route('/usuarios')
def listar_usuarios():
    """
    1. Controle pede os dados ao Modelo
    2. Modelo retorna a lista e usuários
    3. Controle entrega a lista para a Visão renderizazr
    """

    usuarios = usuario_model.get_todos()
    return render_template('usuarios.html', lista_de_usuarios=usuarios)

@app.route('/usuarios/novo', methods =['POST'])
def adicionar_usuario():
    """

    1.CoNTROLE RECEBE OS DADOS DO FORMULÁRIO 
    2.CONTROLE PEDE PARA O MODELO SALVAR OS NOVOS DADOS 
    3. CONTROLE REDIRECIONA O USUÁRIO PARA A PÁGINA PRINCIPAL 

    """

    nome=request.form['nome']
    email=request.form['email']
    usuario_model.salvar(nome, email)
    return redirect(url_for('listar_usuarios'))

if __name__ == '__main__':
    app.run(debug=True)