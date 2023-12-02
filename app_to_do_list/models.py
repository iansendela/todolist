from django.db import models
import uuid


CATEGORIA_CHOICES = [
    ('pessoal','Pessoal'),
    ('estudos','Estudos'),
    ('projetos','Projetos'),
    ('lazer','Lazer'),
    ('trabalho','Trabalho'),
    ('familia','Família'),
    ('saude','Saúde'),
    ('viagem','Viagens'),
    ('social','Social'),
    ('financas','Finanças'),
    ('compras','Compras'),
]


PRIORIDADE_CHOICES = [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'), 
        (4, '★★★★☆'),
        (5, '★★★★★'),  
]

# É uma tabela de tarefas
class Tarefa(models.Model):
    """
    Modelo representando uma tarefa a ser realizada.

    Atributos:
    - id (UUID): Identificador único da tarefa (gerado automaticamente).
    - nome_tarefa (CharField): Nome ou descrição da tarefa (máximo de 255 caracteres).
    - categoria (CharField): Categoria da tarefa escolhida a partir de opções predefinidas.
    - prioridade (IntegerField): Prioridade da tarefa escolhida a partir de opções predefinidas.
    - concluida (BooleanField): Indica se a tarefa foi concluída ou não.
    - data_tarefa_criada (DateTimeField): Data e hora em que a tarefa foi criada (autoinserida na criação).

    Métodos:
    - __str__(): Retorna uma representação de string do nome da tarefa.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome_tarefa = models.CharField(max_length=255)
    categoria = models.CharField(max_length=10, choices=CATEGORIA_CHOICES, default='pessoal')
    prioridade = models.IntegerField(choices=PRIORIDADE_CHOICES, default=3)
    concluida = models.BooleanField(default=False)
    data_tarefa_criada = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_tarefa
    

