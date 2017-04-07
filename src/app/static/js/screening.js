// works on load of screening.html

var seat_view = function(screening_id) {
    window.location.href = "http://127.0.0.1:5000/booking/" + screening_id
}
var slot_fetch = function(date, movie_id) {
    $.ajax({
        url: "http://127.0.0.1:5000/api/screening/date",
        data: {
            date_id: date,
            movie_id: movie_id
        },
        success: function(response) {
            array2 = response.slots;
            var str_full = ""
            var str_head = ""
            var hall_name = ""
            var str_body = ""
            var i;
            for (i = 0; i < array2.length; i++) {
                hall_name = array2[i].hall_name;
                str_head = "<h2 class=\"hall-text\">" + hall_name + "</h2><div class=\"slot-group\">";

                //console.log(array2[i].hall_name);
                while (array2.length > i) {
                    if (array2[i].hall_name != hall_name) {
                        break;
                    }
                    str_body += "<button class=\"slot-button\" onclick = \'seat_view(" + array2[i].screening_id + ")\'><span>" + array2[i].time + "</span></button>";
                    i++;
                }
                //console.log(str_full);
                /* if((array2[i].hall_name) != (hall_name))
                 {
                     continue;
                 }
                 */
                str_full = str_head + str_body;
            }
            $("div.hall-div").html(str_full);
            console.log(array2);
        },
        error: function(response) {
            console.log('Error in fetching slots');
        }
    });
}
$(document).ready(function() {
    var array = [];
    var array2 = [];
    url = window.location.pathname

    var movie_id = url.split("/");
    movie_id = movie_id[2]
    console.log(movie_id);
        //var movie_id = document.getElementsByClassName(movie_id_required)[0].innerHTML;
    $.ajax({
        url: "http://127.0.0.1:5000/api/screening/movies",
        data: "movie_id=" + movie_id,
        success: function(response) {
            array = response.dates;
            //console.log(array);
            var str = "";
            var date = "";
            for (var i = 0; i < array.length; i++) {

             //   print(array[i].date)
               // print(date)
                if (date != array[i].date) {
                    str += '<button class = \"button\" onclick = \'slot_fetch(\"' + array[i].date + '\", ' + movie_id + ');\' >' + array[i].date + '</button>';
                    date = array[i].date;
                }

            }

            $("div.btn-group").html(str);
        },
        error: function(response) {
            console.log('Error in fetching dates');
        }
    });
});

/*var slot_fetch = function(date, movie_id) {
        $.ajax({
            url: "127.0.0.1:5000/api/screening/date",
            data: {
                    date_id : date,
                    movie_id : movie_id
                }
            success: function(response) {
                array2 = response.slots;
                console.log(array2)
            },
            error: function(response) {
                console.log('Error in fetching slots');
            }
        });
*/
//      var str2 = "";            // Now we got audi's in ascending order of their lexicographical name and hence we can loop until a different audi is found or audi's list is finished.....
// This is to be done today.....