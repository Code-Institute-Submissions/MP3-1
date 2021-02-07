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

// show coin details
$('#coin_link').click(function(){
    $('.coin_details').toggle();
})

// toggle description on coin card
// using jquery with jinja2: https://stackoverflow.com/questions/13423646/using-jquery-with-jinja2-to-provide-onclick-event-inside-a-loop-on-each-element
$('.coin_link').each(function(){
    var toggle_div_id = 'coin_details' + $(this).attr('id');
    $('#'+toggle_div_id).hide();
    $(this).click(function(){
        $('#'+toggle_div_id).toggle();
    });
});