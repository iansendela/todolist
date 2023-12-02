from django.shortcuts import render, redirect,get_object_or_404
from .forms import TarefaForm, UpdateTarefaForm
from .models import Tarefa
from django.core.paginator import Paginator



def criar_tarefa(request):
    """
    View para criar uma nova tarefa.

    Se o método da requisição for POST, valida o formulário e salva a nova tarefa.
    Se o método for GET, exibe o formulário vazio para criar uma nova tarefa.

    Redireciona para a página inicial após a conclusão.

    Template: 'paginas_formulario/adicionar.html'
    """

    if request.method == 'POST':
        form = TarefaForm(request.POST)
         # Verifique se o formulário é válido
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TarefaForm()
    return render(request, 'paginas_formulario/adicionar.html', {'form': form})


def home(request):
    """

    View para exibir a lista de tarefas.

    Realiza a filtragem com base nos parâmetros de pesquisa, categoria, prioridade e status.
    Suporta paginação para exibição de tarefas.

    Template: 'to_do_list/home.html'
    """
    termo_pesquisa = request.GET.get('termo_pesquisa', '')  # Obtém o valor do campo de pesquisa
    categoria_selecionada = request.GET.get('categoria', '')
    prioridade_selecionada = request.GET.get('prioridade', '')
    status_selecionado = request.GET.get('status', '')

    tarefas = Tarefa.objects.all()
    paginacao_todas = True  # Variável para controlar a lógica da paginação - mostra todas as tarefas no link do template
    paginacao_filtros = False  # Variável para controlar a lógica da paginação - indica se há filtros aplicados

    # Filtra as tarefas com base no termo de pesquisa
    if termo_pesquisa:
        tarefas = Tarefa.objects.filter(nome_tarefa__icontains=termo_pesquisa)
        paginacao_todas = False

    # Filtra as tarefas com base na categoria
    if categoria_selecionada:
        tarefas = Tarefa.objects.filter(categoria=categoria_selecionada)
        paginacao_todas = False
    
    if prioridade_selecionada:
        tarefas = tarefas.filter(prioridade=int(prioridade_selecionada))
        paginacao_todas = False

    # Filtrar por status
    if status_selecionado == 'a_fazer':
        tarefas = tarefas.filter(concluida=False)
        paginacao_todas = False
    elif status_selecionado == 'feitas':
        tarefas = tarefas.filter(concluida=True)
        paginacao_todas = False

    # Verifica se uma delas é Verdadeira
    if categoria_selecionada or prioridade_selecionada or status_selecionado:
        paginacao_filtros = True
        
    tarefa_paganator = Paginator(tarefas, 5) # primeiro colocamos o tanho e depois o numero de tarefas que eu quero fazer 
    page_num = request.GET.get('page')
    page = tarefa_paganator.get_page(page_num)
    tamanho = len(tarefas)
    context = {
        'page': page,
        'termo_pesquisa': termo_pesquisa,
        'categoria_selecionada': categoria_selecionada,
        'prioridade_selecionada': prioridade_selecionada,
        'status_selecionado': status_selecionado,
        'paginacao': paginacao_todas,
        'paginacao_filtros': paginacao_filtros,
        'tamanho': tamanho
    }
    return render(request, 'to_do_list/home.html', context)



def editar_tarefa(request, id_tarefa):
    """
    View para editar uma tarefa existente.

    Se o método da requisição for POST, valida o formulário e salva as alterações na tarefa.
    Se o método for GET, exibe o formulário preenchido com os dados da tarefa a ser editada.

    Redireciona para a página inicial após a conclusão.

    Template: 'paginas_formulario/editar_tarefa.html'
    """

    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    if request.method == 'POST':
        form = UpdateTarefaForm(request.POST, instance=tarefa)
        # Verifique se o formulário é válido
        if form.is_valid():
            # Salve as alterações na tarefa
            form.save()
            return redirect('home')
    else:
        form = UpdateTarefaForm(instance=tarefa)

    return render(request, 'paginas_formulario/editar_tarefa.html', {'form': form, 'tarefa': tarefa})


# função para deletar a tarefa
def delete(request, id_tarefa):
    """
    View para excluir uma tarefa.

    Obtém a tarefa pelo ID, exclui e redireciona para a página inicial.

    Redireciona para a página inicial após a conclusão.
    """
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    tarefa.delete()
    return redirect('home')

# função para concluir a tarefa
def concluida(request, id_tarefa):
    """
    View para marcar uma tarefa como concluída.

    Obtém a tarefa pelo ID, marca como concluída e redireciona para a página inicial.

    Redireciona para a página inicial após a conclusão.
    """
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    tarefa.concluida = True
    tarefa.save()
    return redirect('home')

# função para desmarcar a tarefa
def desmarcar_concluida(request, id_tarefa):
    """
    View para desmarcar uma tarefa como concluída.

    Obtém a tarefa pelo ID, desmarca como concluída e redireciona para a página inicial.

    Redireciona para a página inicial após a conclusão.
    """
    tarefa = get_object_or_404(Tarefa, id=id_tarefa)
    tarefa.concluida = False
    tarefa.save()
    return redirect('home')
