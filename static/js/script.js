$(document).ready(function () {
    // hide user coins in profile page
    $('#user_coins').hide(); 
})

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

 // show user coins in profile page
$('#show_coins').click(function(){
    $('#user_coins').toggle();
    $('#show_coins').html("Hide coins");
})