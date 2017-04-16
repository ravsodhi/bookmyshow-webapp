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
    var x = window.location.href;
    x =  x.split("/")
    x = x[0] + "//" + x[2] + "/" + "booking/" + screening_id
    window.location.href = x
}

function slot_fetch(date, movie_id) {
    $.ajax({
        url: "/api/screening/date",
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
            if(array2.length == 0)
            {
                str_full = "<h2 class=\"hall-text\">No Shows Available</h2>";
            }
            for (i = 0; i < array2.length; i++) {
                hall_name = array2[i].hall_name;
                var str_body = ""

                str_head = "<h2 class=\"hall-text\">" + hall_name + "</h2><div class=\"slot-group\">";

                //console.log(array2[i].hall_name);
                while (array2.length > i) {
                    if (array2[i].hall_name != hall_name) {
                        break;
                    }
                    time = array2[i].time;
                    ti = time.split(":")
                    console.log(ti)
                    ti[0] = parseInt(ti[0])
                        //ti[1] = parseInt(ti[1])
                    console.log(ti)

                    if (ti[0] > 12) {
                        ti[0] = ti[0] - 12
                        fti = ti[0].toString() + ":" + ti[1] + ' PM'
                    } else {
                        if (ti[0] < 12) {
                            fti = ti[0].toString() + ":" + ti[1] + ' AM'
                        } else {
                            fti = ti[0].toString() + ":" + ti[1] + ' PM'
                        }
                    }
                    console.log(ti[0])
                    console.log(fti)
                        //if(time[0])

                    str_body += "<button class=\"slot-button\" onclick = \'seat_view(" + array2[i].screening_id + ")\'><span>" + fti + "</span></button>";
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

function loader() {
    var array = [];
    movieid = parseInt(window.location.pathname.split("/")[2])
    tempAlert("Page is Loading", 2000)
        //var movie_id = document.getElementsByClassName(movie_id_required)[0].innerHTML;
    $.post({
        url: "/api/screening/movies",
        data: {
            movie_id: movieid
        },
        success: function(response) {
            console.log("success")
            array = response.dates;
            console.log(array)

            var str = "";
            var date = "";
            for (var i = 0; i < array.length; i++) {
                temp = array[i].date.split("-")
                temp = temp[2] + "-" + temp[1] + "-" + temp[0]
                if (date != array[i].date) {
                    str += '<button class = \"button\" onclick = \'slot_fetch(\"' + array[i].date + '\", ' + movieid + ');\' >' + temp + '</button>';
                    date = array[i].date;
                }

            }

            $("div.btn-group").html(str);
            slot_fetch(array[0].date, movieid);
            console.log(movieid)

        },
        error: function(response) {
            console.log('Error in fetching dates');
        }
    });
};

loader()
