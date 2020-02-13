const $ = window.$;
$('DIV#toggle_header').click(function () {
  if ($('HEADER').hasClass('red')) {
    $('HEADER').removeClass('red');
    $('HEADER').addClass('green');
  } else {
    $('HEADER').removeClass('green');
    $('HEADER').addClass('red');
  }
});
