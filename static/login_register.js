// On Click SignUp It Will Hide Login Form and Display Registration Form
$(document).ready(function(){
  $("#register_form").hide();
  $("#login_form").hide();
});

$("#register").click(function() {
$("#register_form").slideDown("slow");
$("#register_form").css("visibility","visible");
$("#login_form").hide();
$(".content").css("opacity","0.3");
});

// On Click SignIn It Will Hide Registration Form and Display Login Form
$("#signin").click(function() {
$("#login_form").slideDown("slow");
$("#login_form").css("visibility","visible");
$("#register_form").hide();
$(".content").css("opacity","0.3");
$("#error").hide();
});

//function validation(){ 
    //if(document.getElementById('id_username') == ""){   //checking if the form is empty
       //$("#error").show();
    //return false;
    //}
//}
