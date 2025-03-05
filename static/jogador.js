$(".jogador-excluir").click(function () {
  $.ajax({
    type: 'POST',
    url: "/excluir-jogador",
    data: { nome: 'teste' },
    dataType: "text",
    success: function (data) {
      console.log("Jogador Excluído");
      event.preventDefault()
      redirecionar_jogador()
    }
  });
});

function redirecionar_jogador() {
  $.ajax({
    type: 'GET',
    url: "/jogador",
    dataType: "text",
    success: function (data) {
      console.log("Jogador Excluído");
    }
  });
}