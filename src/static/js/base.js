
$('.button-collapse').sideNav({
      menuWidth: 300, // Default is 300
      edge: 'right', // Choose the horizontal origin
      closeOnClick: false, // Closes side-nav on <a> clicks, useful for Angular/Meteor
      draggable: true, // Choose whether you can drag to open on touch screens,
      onOpen: function(el) { }, // A function to be called when sideNav is opened
      onClose: function(el) {  }, // A function to be called when sideNav is closed
    }
    );

$(document).ready(function(){
    $('.slider').slider();
    $('.slider').slider('start');
    $(window).load(function() {
      $('.peeek-loading').delay(1000).fadeOut(1500);
    });
  });
