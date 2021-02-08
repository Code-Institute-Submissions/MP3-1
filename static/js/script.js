$(document).ready(function () {
    // hide user coins in profile page
    $('#user_coins').hide();
    $('#hide_coins_btn').hide();
    // counters
    $('.count-up').counter();
    $('.count1').counter();
    $('.count2').counter();
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

// counter from: https://mdbootstrap.com/snippets/jquery/marta-szymanska/1363695#js-tab-view
(function ($){
  $.fn.counter = function() {
    const $this = $(this),
    numberFrom = parseInt($this.attr('data-from')),
    numberTo = parseInt($this.attr('data-to')),
    delta = numberTo - numberFrom,
    deltaPositive = delta > 0 ? 1 : 0,
    time = parseInt($this.attr('data-time')),
    changeTime = 10;
    
    let currentNumber = numberFrom,
    value = delta*changeTime/time;
    var interval1;
    const changeNumber = () => {
      currentNumber += value;
      //checks if currentNumber reached numberTo
      (deltaPositive && currentNumber >= numberTo) || (!deltaPositive &&currentNumber<= numberTo) ? currentNumber=numberTo : currentNumber;
      this.text(parseInt(currentNumber));
      currentNumber == numberTo ? clearInterval(interval1) : currentNumber;  
    }

    interval1 = setInterval(changeNumber,changeTime);
  }
}(jQuery));