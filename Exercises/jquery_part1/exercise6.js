$(document).ready(function () {
    $("#addButton").click(function(){
      $("#playlist").append(
        "<li>" + $("#songTextInput").val() + "</li>"
      );
    });
});
