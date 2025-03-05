$(".excluir-jogador").click(function() {
   $.ajax({
        type: 'POST',
        url: "excluir-jogador",
        data: {nome: 'teste'},
        dataType: "text"
   })
})