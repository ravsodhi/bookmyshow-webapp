$(document).ready(function() {
	console.log("index.js")
    $.ajax({
        url: 'http://127.0.0.1:5000/api/movies',
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
            for (var i = 0; i < array.length; i++) {
               // str += '<li>' + array[i].title + '<button type=\'button\' onclick=\'book(\"' + array[i].id + '\");\'>'
               // '</li>';
                str2 += '<br/> <div class=\"list-type3 movie-box\"> <div style=\"float:left;"> <h2>' + array[i].title + '</h2> <br/> <h4>' + array[i].description + '</h4> </div> <br/> <br/> <li style=\"float:right\"> <a href=\"#\" onclick=\"book(' + array[i].id + '); \">Book Now</a></li> </div><br/>';
            }
            $("div.movie-div").html(str2);
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
    /*
    $.ajax({
        url: 'http://127.0.0.1:5000/api/screening',
        method: 'GET',
        data: "movie_id=" + id,
        success: function(response) {
      */      window.location.href = 'http://127.0.0.1:5000/movie/' + id
            //document.write(response)
       /* },
        error: function(response) {
            console.log(response);
        }
    });*/
}
