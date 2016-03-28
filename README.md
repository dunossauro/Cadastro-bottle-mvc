# Cadastro-bottle-mvc

> Um projeto totalmente despretencioso e estupidamente simples

O Objetivo desse projeto é mostrar a simples interação entre SQLite3 e Bottle para os iniciantes.


### Data.py

O arquivo data.py tem uma classe simples para importação no arquivo de controle e dispoões de algumas operações simples de SQL como Busca e Inserção

#### Busca
```
from Data import Base
db = Base()
data = db.busca   #Retorna uma lista de tuplas do banco
```

#### Inserção
```
from Data import Base
db = Base()
db.inserir(<val_1>,<val_2>)
db.commit()
```
