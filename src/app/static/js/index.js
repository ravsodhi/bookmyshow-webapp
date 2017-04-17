$(document).ready(function() {
    console.log("index.js")
     

    $.ajax({
        url: '/api/movies',
        method: 'GET',
        data: {},
        success: 
        function(response) {
            console.log(response)
            if(response.success)
            {
                var str = "";
            var str2 = "";
            var array = response.movies;
            var upMovies = response.upmovies;
            for (var i = 0; i < array.length; i++) {
                str2 += '<br/> <div class=\"list-type3 movie-box\"> <div style=\"float:left;"> <h2 style=\"font-family:\'Macondo\'\">' + array[i].title + '</h2> <br/> <h4>' + array[i].description + '</h4> </div> <br/> <br/> <li style=\"float:right\"> <a href=\"#\" onclick=\"book(' + array[i].id + '); \">Book Now</a></li> </div><br/>';
            
            }
            var str3 = "";

            for (var i = 0; i < upMovies.length; i++) {
                str3 += '<br/> <div class=\"list-type3 movie-box\"> <div style=\"float:left;"> <h2 style=\"font-family:\'Macondo\'\">' + upMovies[i].title + '</h2> <br/> <h4>' + upMovies[i].description + '</h4> </div></div>';

            }
            if(array.length == 0)
            {
                str2 = "<h2 class style=\'color:white;font-family:\'Macondo\'\'>No Shows Available</h2>";
            }
            if(upMovies.length == 0)
            {
                str3 = "<h2 class style=\'color:white;font-family:\'Macondo\'\'>No Shows Available</h2>";

            }
            $("div.movie-div").html(str2);
            $("div.up-movie-div").html(str3);

        }
        },
        error: function(response) {
            console.log(response)
            var message = "Unable to fetch movies";
            $("div.movie-div").html(message);
        }
    });

});

var book = function(id /* This is the id of movie*/ ) {
       var x = window.location.href;
        x =  x.split("/")
        x[3] = "movie/" + id
        x = x.join("/")
       window.location.href = x
}
    

