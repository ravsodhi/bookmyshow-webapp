// works on load of screening.html
function tempAlert(msg, duration) {

    var el = document.createElement("div");
    el.innerHTML = msg;
    el.setAttribute("style", "position:fixed ; top:87% ;bottom:5%; left:45% ; background-color:black ; height:9%;padding: 12px 20px;color:white;");
    setTimeout(function() {
        el.parentNode.removeChild(el);
    }, duration);
    document.body.appendChild(el);
}

function seat_view(screening_id) {
    window.location.href = "http://127.0.0.1:5000/booking/" + screening_id
}

function slot_fetch(date, movie_id) {
    $.ajax({
        url: "http://127.0.0.1:5000/api/screening/date",
        data: {
            date_id: date,
            movie_id: movie_id
        },
        method: 'POST',
        success: function(response) {
            array2 = response.slots;
            var str_full = ""
            var str_head = ""
            var hall_name = ""
            var i;
            for (i = 0; i < array2.length; i++) {
                hall_name = array2[i].hall_name;
                var str_body = ""

                str_head = "<h2 class=\"hall-text\">" + hall_name + "</h2><div class=\"slot-group\">";

                //console.log(array2[i].hall_name);
                while (array2.length > i) {
                    if (array2[i].hall_name != hall_name) {
                        break;
                    }
                    str_body += "<button class=\"slot-button\" onclick = \'seat_view(" + array2[i].screening_id + ")\'><span>" + array2[i].time + "</span></button>";
                    i++;
                }
                i--;

                str_full += str_head + str_body + "</div>"
            }
            $("div.hall-div").html(str_full);
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
    tempAlert("Page is Loading", 2000)
        //var movie_id = document.getElementsByClassName(movie_id_required)[0].innerHTML;
    $.ajax({
        url: "http://127.0.0.1:5000/api/screening/movies",
        method: 'POST',
        data: {
            movie_id: movie_id
        },
        success: function(response) {
        	console.log("success")
            array = response.dates;
            var str = "";
            var date = "";
            for (var i = 0; i < array.length; i++) {
                if (date != array[i].date) {
                    str += '<button class = \"button\" onclick = \'slot_fetch(\"' + array[i].date + '\", ' + movie_id + ');\' >' + array[i].date + '</button>';
                    date = array[i].date;
                }

            }

            $("div.btn-group").html(str);
            slot_fetch(array[0].date, movie_id);
        },
        error: function(response) {
            console.log('Error in fetching dates');
        }
    });
});
