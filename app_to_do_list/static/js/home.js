$(document).ready(function () {
    $('#id_categoria').change(function () {
        this.form.submit(); // é para submeter automaticamente sempre que eu selecionar uma nova categoria assim não vai precisar que eu clique sempre no botão para ele mostrar os dados com base na categoria
    });

    $('#id_prioridade').change(function () {
        this.form.submit();
    });

    $('#id_status').change(function () {
        this.form.submit();
    });
});

