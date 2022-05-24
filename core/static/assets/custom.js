
$('#aceita_publica').change(function () {
    console.log(this.checked)
    if (this.checked) {
        $('#div-temas').addClass('hidden');
        $('#div-categoria').removeClass('hidden');
    } else {
        $('#div-temas').removeClass('hidden');
        $('#div-categoria').addClass('hidden');
    }

});

