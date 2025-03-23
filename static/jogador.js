
 
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
      let qtdItems = $(".table-responsive table tbody tr").length
      if (qtdItems == 0) {
          $(".table-responsive").remove()
      }
      
      $(".alert-danger").css("visibility", "visible");
      setTimeout(function() {
        $(".alert-danger").css("visibility", "hidden")
      }, 1000);
    },
      error: function(error) {
        console.log("Error:", error);
    }
  });
});



$(".jogador-editar").click(function () {

  let idjogador = $(this).attr("value")
  
  $.ajax({
    type: 'GET',
    url: "/editar-jogador/".concat(idjogador),
    dataType: "text",
    success: function() {
      
    },
      error: function(error) {
        console.log("Error:", error);
    }
  });
});

