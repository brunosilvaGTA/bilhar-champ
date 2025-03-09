$(".jogador-excluir").click(function () {

  let idJogador = $(this).attr("value") 
  let listItem = $(this).parent().parent()

  $.ajax({
    type: 'POST',
    url: "/excluir-jogador",
    data: {'id_jogador': idJogador },
    dataType: "text",
    success: function() {
      listItem.remove(); 
      $(".alert-danger").css("visibility", "visible");
      setTimeout(function() {
        $(".alert-danger").css("visibility", "hidden")
      }, 1000);
    },
    error: function(error){
      console.log("Error", error)
    }
  });
});


$(".jogador-editar").click(function () {

  let idJogador = $(this).attr("value") 

  $.ajax({
    type: 'POST',
    url: "/editar-jogador",
    data: {'jogador': idJogador },
    dataType: "text",
    success: function() {
      
    },
    error: function(error){
      console.log("Error", error)
    }
  });
});



