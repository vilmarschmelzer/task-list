# task-list
Aplicativo web de lista de tarefas

###1. Este projeto será desenvolvido utilizando:

* Python 3
* Django 1.9
* REST
* Sqlite
* AngularJS
* Bootstrap 3

###2. Instalação (utilizando virtualenv)

  Criar virtualenv para Python 3
  
  ```virtualenv nome_virtualenv -p python3```
  
  Inicia virtualenv
  
  ```source diretorio da virtualenv/bin/activate```
  
  No projeto esta incluído o requirements.txt, para facilitar a instalação das dependências
  
  ```pip3 install -r requirements.txt```

###3. Execução

  Vá ao diretório onde foi clonado o projeto e execute o comando
  
  ```python manager.py runserver```

###4. Logs

  Os logs são registrados no diretório raiz do projeto, com o nome 'task_list.log'

###5. Testes

  * Campos da tarefa
  
    id: identificador da tarefa

    task: descrição da tarefa
    
    done: 'true' para tarefa finalizada, 'false' para tarefa não finalizada 
      
  * Inserir nova tarefa
  
  ```curl -X POST -H "Content-Type: application/json" -d '{"task": "descrição da tarefa", "done": false}' http://localhost:porta/task/```
        
  * Editar tarefa, para editar é necessário passar o id da tarefa
  
  ```curl -X POST -H "Content-Type: application/json" -d '{"id":50,"task": "descrição da tarefa", "done": false}' http://localhost:porta/task/```

    Quando informado o id da tarefa não existente na base de dados, retornara o erro 404 com a mensagem 'Tarefa não encontrada para atualizar'
      
  * Listar tarefas
  
  ```curl -X GET http://localhost:porta/task/```
  
  * Buscar tarefa, ID = id da tarefa
    
  ```curl -X GET http://localhost:porta/get-task/ID/```
    
    Caso o id informado não existir, retornara o erro 404 com a mensagem 'Tarefa não encontrada'

  * Finalizar tarefa, ID = id da tarefa
  
  ```curl -X GET http://localhost:porta/done-task/ID/```

    Caso o id informado não existir, retornara o erro 404 com a mensagem 'Tarefa não encontrada'
  
  * Excluir tarefa, ID = id da tarefa

  ```curl -X DELETE http://localhost:porta/task/ID/```
  
    Caso o id informado não existir, retornara o erro 404 com a mensagem 'Tarefa não encontrada'
