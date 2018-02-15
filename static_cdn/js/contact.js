setTimeout(function() {
  $('.present').toggleClass('tada');
  $('.title').toggleClass('tada2');
},2000);

$('.toggle-tada').click(function() {
  $('.present').toggleClass('tada');
  $('.title').toggleClass('tada2');
});