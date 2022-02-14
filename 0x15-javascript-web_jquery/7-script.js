$(function() {
    $.get('https://swapi-api.hbtn.io/api/people/5/?format=json',
	  function(data, textStatus) {
	      $('DIV#character').text(data.name);
	  });
});
