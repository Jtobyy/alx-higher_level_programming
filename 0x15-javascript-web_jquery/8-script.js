$(function() {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json',
	  function(data, textStatus) {
	      films = data.results;
	      $.each(films, function(i, film) {
		  $('UL#list_movies').append('<li>'+film.title+'</li');
	      });
	  });
});
