$(document).ready(function () {
    // hide user coins in profile page
    $('#user_coins').hide();
    $('#hide_coins_btn').hide();
})
// tooltiop function
$(function () {
  $('[data-toggle="tooltip"]').tooltip()
})

 // show user coins in profile page
$('#show_coins_btn').click(function(){
    $('#show_coins_btn').hide();
    $('#hide_coins_btn').show();
    $('#user_coins').show(); 
})

 // hide user coins in profile page
$('#hide_coins_btn').click(function(){
    $('#hide_coins_btn').hide();
    $('#show_coins_btn').show();
    $('#user_coins').hide(); 
})