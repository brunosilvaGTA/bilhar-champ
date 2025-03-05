
 
$(".jogador-excluir").click(function () {

   
  let itemValue = $(this).attr("value")
  let listItem = $(this).parent().parent()
  
  $.ajax({
    type: 'POST',
    url: "/excluir-jogador",
    data: {'nome': itemValue },
    dataType: "text",
    success: function (data) {
      listItem.remove();
    },
      error: function(error) {
        console.log("Error:", error);
    }
  });
});

// function redirecionar_jogador() {
//   $.ajax({
//     type: 'GET',
//     url: "/jogador",
//     dataType: "text",
//     success: function (data) {
//       console.log("Jogador Excluído");
//     }
//   });
// }