$(document).ready(function() {
    $.ajax({
        url: '127.0.0.1:5000/api/movies',
        method: 'GET',
        data: {},
        success: function(response) {
            var str = "";
            var str2 = "";
            var array = response.movies;
            for (var i = 0; i < array.length; i++) {
                str += '<li>' + array[i].movie + '<button type=\'button\' onclick=\'book(\"' + response[i].id + '\");\'>'
                '</li>';
                str2 += '<br/> <div class=\"list-type3 movie-box\"> <div style=\"float:left;"> <h2>' + array[i].name + '</h2> <br/> <h4>' + array[i].description + '</h4> </div> <br/> <br/> <li style=\"float:right\"> <a href=\"#\" onclick=\"book(' + array[i].id + '); \">Book Now</a></li> </div><br/>';
            }
            $("div#movie-div").html(str2);
        },
        error: function() {
            var message = "Unable to fetch movies";
            $("div#movie-div").html(message);
        }
    });
});

var book = function(id /* This is the id of movie*/ ) {
    $.ajax({
        url: '127.0.0.1:5000/api/booking',
        method: 'GET',
        data: "id:" + id,
        success: function(response) {
            console.log(response);
        },
        error: function(response) {
            console.log(response);
        }
    });
}
