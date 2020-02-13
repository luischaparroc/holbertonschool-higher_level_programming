$.get("https://swapi.co/api/films/?format=json", function(data, textStatus) {
    let res = data.results;
    for (let i = 0; i < res.length; i++) {
	$("UL#list_movies").append("<li>" + res[i].title + "</li>");
    }
});
