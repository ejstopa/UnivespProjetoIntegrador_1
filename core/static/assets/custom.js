
$('#aceita_publica').change(function () {
    if (this.checked) {
        $('#div-temas').addClass('hidden');
        $('#div-categoria').removeClass('hidden');
    } else {
        $('#div-temas').removeClass('hidden');
        $('#div-categoria').addClass('hidden');
    }

});

function moouseOverComponent(element){
    console.log('mouse Over Funcion');
    let viewElement = element.target
    console.log(viewElement);
    stop

  /*  $.ajax({
        url: "./../../readText/" ,
        type: "get",
        datatype: "html",
        data: { var1: "fo1", var2: "fo2" },
        success: function(response){
                console.log("OK"); 
        }
    });*/
};

$('.element_for_read').on('mouseover', function(){
    console.log('mouse Over');
    let viewElement = $(this).contents()
    let text = encodeURI(viewElement[0]['data'])
    console.log(viewElement[0]['data']);

    $.ajax({
        url: "./../../readText/" ,
        type: "get",
        datatype: "html",
        data: { text: text },
        success: function(response){
                console.log("OK"); 
        }
    });
})