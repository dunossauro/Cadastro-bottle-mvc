from bottle import run, template, route, view, post, request
import socket
from Data import Base

ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close())
  for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]

# ------ Classe de representação dos estados sem view
class Repr:
    def __init__(self):
        self.error = """Aconteceu algum erro, tente efetuar a operação outra vez
                        <br>
                        <br>
                        <br>
                        <a href="/">Voltar a home</a>"""

        self.ok = """OK
                    <br>
                    <br>
                    <br>
                    <a href="/">Voltar a home</a>
                    """

@route('/')
@view('view/home.html')
def home():
    return dict(title ="Home")

@route('/cadastro')
@view('view/cadastro.html')
def cadastro():
    return dict(title ="Cadastro")

@post('/cadastro')
def cadastro():
    db = Base()
    nome = request.forms.get('nome')
    email = request.forms.get('mail')
    try:
        assert nome != ''
        assert email != '' and "@" in email
        db.inserir_dados(nome,email)
        db.commit()
        saida = Repr()
        return saida.ok
    except:
        saida = Repr()
        return saida.error

@route('/base')
@view('view/base.html')
def base():
    try:
        db = Base()
        data = db.busca()
        assert data[0]
        return template('view/base', rows=data)
    except:
        saida = Repr()
        return saida.error

run(host=ip, port=8080)
