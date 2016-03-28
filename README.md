# Cadastro-bottle-mvc

> Um projeto totalmente despretencioso e estupidamente simples

O Objetivo desse projeto é mostrar a simples interação entre SQLite3 e Bottle para os iniciantes.


## Data.py

O arquivo data.py tem uma classe simples para importação no arquivo de controle e dispoões de algumas operações simples de SQL como Busca e Inserção

### Busca
```
from Data import Base
db = Base()
data = db.busca   #Retorna uma lista de tuplas do banco
```

### Inserção
```
from Data import Base
db = Base()
db.inserir(<val_1>,<val_2>)
db.commit()
```
## Control.py

O arquivo Control.py é a interface de controle entre as Views do sistema e as requisições no banco de dados.

### Comandos do Bottle

```
from bottle import post, request

@route('/')                                       #Diz qual a URL vai retornar a view da linha inferior
@view('view/home.html')                           #Endereço da view no sistema de arquivos
def func(args):                                   #Função a ser executada pelo controle
  return template('view/base', <var>=<data>)      #Retorna um teplate do sistema de arquivos com as alterações das variáveis

@post('/')                                        #Função que corresponde ao metodo Post usado em alguma view
def func(args):
  pass

run(host=<IP>, port=<Porta>)                      #Sobe um servidor WSGIRefServer na porta e IP inseridos na função
```
