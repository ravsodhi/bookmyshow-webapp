function viewMovies()
{
	var str_table = "";
	var i;
	for(i=0;i<allMovies.length;i++)
	{
		str+="<tr><td>"
		+ allMovies[i].name+
		"</td></tr>"
		
	}
	$('#allMovies tbody').html(str_table);
}

function fetchMovies()
{
	var str ="";
	var i;
	$.ajax({
		url:"127.0.0.1/movies",
		method: 'GET',
		success: function(response)
		{
			allMovies = response.movies;
			viewMovies();
		}
		error: function(response)
		{
			console.log("Error: Unable to fetch movies from datebase");
		}
	});
}	