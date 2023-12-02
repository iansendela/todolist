from django import forms
from .models import Tarefa



class TarefaForm(forms.ModelForm):
    """
    Formulário para criar uma nova tarefa.

    Utiliza o modelo Tarefa e inclui campos para o nome da tarefa, categoria e prioridade.

    Meta:
    - model (Tarefa): Modelo associado ao formulário.
    - fields: Campos do modelo a serem incluídos no formulário.
    """
    class Meta:
        model = Tarefa
        fields = ['nome_tarefa', 'categoria', 'prioridade']


class UpdateTarefaForm(forms.ModelForm):
    """
    Formulário para editar uma tarefa existente.

    Utiliza o modelo Tarefa e inclui campos para o nome da tarefa, categoria, prioridade e status de conclusão.

    Meta:
    - model (Tarefa): Modelo associado ao formulário.
    - fields: Campos do modelo a serem incluídos no formulário.
    """
    class Meta:
        model = Tarefa
        fields = ['nome_tarefa', 'categoria', 'prioridade', 'concluida']