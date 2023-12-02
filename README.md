# Gerenciador de Tarefas Django

Bem-vindo ao Gerenciador de Tarefas Django! Este é um aplicativo simples de lista de tarefas construído em Django que permite aos usuários criar, editar, excluir e marcar como concluídas suas tarefas diárias.

## Requisitos

- Python 3.x
- Django 3.x


## Instruções de Configuração

1. Clone o Repositório:
 - git clone https://github.com/seu-usuario/gerenciador-de-tarefas-django.git
   cd gerenciador-de-tarefas-django


2. Crie um Ambiente Virtual
- python -m venv venv


3. Ative o Ambiente Virtual
- source venv/bin/activate # (Linux/Mac)
- venv\Scripts\activate # (Windows)


4. Instale as Dependências
    - pip install -r requirements.txt


5. Aplique as Migrações
    - python manage.py migrate


6. Execute o Servidor
    - python manage.py runserver
    

7. Acesse o Aplicativo
- Abra o navegador e visite `http://127.0.0.1:8000/`


## Funcionalidades

- Adicione novas tarefas com nome, categoria e prioridade.
- Filtragem de tarefas por termo de pesquisa, categoria, prioridade e status (a fazer/feitas).
- Paginação para visualização de tarefas.
- Edite tarefas existentes.
- Marque tarefas como concluídas ou desmarque como não concluídas.
- Exclua tarefas.


## Estrutura do Projeto

- `Gerenciador_de_tarefas/`: Configurações principais do Django.
- `app_to_do_list/`: Aplicativo de lista de tarefas.
- `templates/`: Templates HTML para renderização das páginas.
- `static/`: Arquivos estáticos (CSS, JS).
- `db.sqlite3`: Banco de dados SQLite3 (incluído para simplicidade).


## Conclusão

Este é um projeto Django básico que pode ser estendido e aprimorado conforme necessário. Sinta-se à vontade para explorar, contribuir e adaptar conforme suas necessidades específicas. Se precisar de ajuda ou tiver sugestões, sinta-se à vontade para entrar em contato!


**Agradecimentos:**
Agradecemos por usar o Gerenciador de Tarefas Django. Esperamos que seja útil e eficiente na organização das suas atividades diárias.
