# task-list
Aplicativo web de lista de tarefas

###1. Este projeto será desenvolvido utilizando:

* Python 3
* Django 1.9
* Sqlite
* AngularJS
* Bootstrap 3

###2. Instalação (Utilizando virtualenv)

  Criar virtualenv
  
  ```virtualenv nome_virtualenv -p python3```
  
  No projeto incluído o requirements.txt, para facilitar a instalação das dependências
  
  ```pip3 install -r requirements.txt```

###3. Execução
  Vá ao diretorio onde foi clonado o projeto e execute o comando
  
  ```python manager.py runserver```

###4. Testes
      Cmapos da tarefa
        id: identificador da tarefa
        task: descrição da tarefa
        done: 'true' para tarefa finalizada, 'false' para tarefa não finalizada 
      
      * Cadastrar nova
        ```curl -X POST -H "Content-Type: application/json" -d '{"task": "descrição da tarefa", "done": false}' http://localhost/task/```
        
      * Editar tarefa, para editar é necessario passar o id da tarefa
        ```curl -X POST -H "Content-Type: application/json" -d '{"id":50,"task": "descrição da tarefa", "done": false}' http://localhost/task/```
      
      * Listar tarefas
      
      * Finalizar tarefa
      
      * Excluir tarefa
      
  
