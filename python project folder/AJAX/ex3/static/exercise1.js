
$(document).ready(function(){
  $("input[username=username]").blur(function(){
    $.get("/check_username", {username: $(this).val()}, function(data){
      $("#username_status").val(data);
    });
  });
});
