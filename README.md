# Task Manager API

Este repositório é referente a um desafio técnico no qual tem como seu principal objetivo criar um CRUD para gerenciar tarefas.

## Instruções de uso

Antes de tudo, caso você tenha o postgresql instalado em sua máquina configure o arquivo `.env` com as informações de conexão para assim poder executar as demais configurações.

Caso queira usar um banco sqlite basta alterar as configurações no arquivo `configs/settings/development.py`.

1º)Criação de um ambiente e ativação de umvirtual 
> Linux:

Criação
~~~
python3 -m venv venv
~~~
Ativação:
~~~
. venv/bin/activate
~~~

> Windows:

Criação:
~~~
python -m venv venv
~~~
Ativação:
~~~
venv\Scripts\activate
~~~

2º) Instalação de dependências
~~~
pip install -r requirements.txt
~~~

3º) Migração para o banco de dados
~~~
python manage.py makemigrations
~~~
Logo depois:
~~~
python manage.py migrate
~~~

4º) Criação do super usuário
~~~
python manage.py createsuperuser
~~~

5º) Inicialização da aplicação
~~~
python manage.py runserver
~~~
6º) Documentação da API:
~~~
http://localhost:8000/docs/
~~~