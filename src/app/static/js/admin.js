function tempAlert(msg, duration) {

    var el = document.createElement("div");
    el.innerHTML = msg;
    el.setAttribute("style", "position:fixed ; top:87% ;bottom:5%; left:45% ; background-color:black ; height:9%;padding: 12px 20px;color:white;");
    setTimeout(function() {
        el.parentNode.removeChild(el);
    }, duration);
    document.body.appendChild(el);
}

function addMovie() {
    title = document.forms[0].elements[0].value;
    director = document.forms[0].elements[1].value;
    discription = document.forms[0].elements[2].value;
    duration = document.forms[0].elements[4].value;
    urli = document.forms[0].elements[3].value;
    $.ajax({
        url: "http://127.0.0.1:5000/api/movie/add",
        method: 'POST',
        data: {
            title: title,
            director: director,
            discription: discription,
            duration: duration,
            url: urli,
        },
        success: function(response) {
            console.log("movie added")
            tempAlert("Movie Added", 2500)

        },
        error: function(response) {
            console.log('Error in adding movie');
            tempAlert("Error in adding Movie", 2500)

        }
    });
}

function addHall() {
    console.log("hello")
    k = document.forms[2].elements[0].value;
    console.log(k)
    l = document.getElementsByClassName('addhall')[0]
    l = l.selectedOptions;
    l = l[0].value;
    console.log(l)
    $.ajax({
        url: "http://127.0.0.1:5000/api/auditorium/add",
        method: 'POST',
        data: {
            name: k,
            audi_type: l,
        },
        success: function(response) {
            console.log("Auditorium added")
            tempAlert("Auditorium Added", 2500)
        },
        error: function(response) {
            console.log('Error in adding Auditorium');
            tempAlert("Error in adding Auditorium", 2500)
        }
    });

}

function selectHall() {
    console.log("hello")
    k = document.getElementsByClassName('selecthall')[0]
    k = k.selectedOptions;
    m = ""
    time = ""

    for (i = 0; i < k.length; i++)
        if (i != k.length - 1)
            m += k[i].value + ","
        else
            m += k[i].value
    k = document.getElementsByClassName('selecttime')[0]
    k = k.selectedOptions;
    for (i = 0; i < k.length; i++)
        if (i != k.length - 1)
            time += k[i].value + ","
        else
            time += k[i].value
    k = document.getElementById('selectmovie').value
    idi = k
    date1 = document.getElementById('release_date').value
    date2 = document.getElementById('off_theatre_date').value

    $.post({
        url: "http://127.0.0.1:5000/api/screening/add",
        data: {
            audi_id: m,
            time: time,
            rel_date: date1,
            off_date: date2,
            movie_id: idi
        },
        success: function(response) {
            console.log("success in adding screening")
            tempAlert("Screening Added", 2500)
        },
        error: function(response) {
            console.log("error ")
            tempAlert("Error in adding screening", 2500)

        }


    });

}
$(document).ready(function() {

    $.ajax({
        url: "http://127.0.0.1:5000/api/auditorium",
        success: function(response) {
            console.log(response.audi)
            auditoriums = response.audi;
            str = ""
            for (var i = 0; i < auditoriums.length; i++) {
                hall_type = auditoriums[i].audi_type;
                var str_body = ""
                str_head = "<optgroup label=" + hall_type + ">"
                while (auditoriums.length > i) {
                    if (auditoriums[i].audi_type != hall_type)
                        break;
                    str_body += "<option value=\"" + auditoriums[i].id + "\">" + auditoriums[i].name + "</option>";
                    i++;
                }
                i--;
                str += str_head + str_body + "</optgroup>"
            }
            console.log(str)
            $("select.selecthall").html(str);
            tempAlert("Form is loading", 2500)
        },
        error: function(response) {
            console.log("Error in fetching auditoriums")
            tempAlert("Error in fetching auditoriums", 2500)

        }
    })
})

var movieFetcher = function() {
    $.ajax({
        url: "http://127.0.0.1:5000/api/movies",
        success: function(response) {
            console.log(response.audi)
            movies = response.movies;
            str = ""
            for (var i = 0; i < movies.length; i++) {
                str += "<option value=\"" + movies[i].id + "\">" + movies[i].title + "</option>";
            }
            console.log(str)
            $("select#selectmovie").html(str);
        },
        error: function(response) {
            console.log("Error in fetching movies")
            tempAlert("Error in fetching movies", 2500)

        }
    })
}

function addCost(){
    cost1 = $("input#platinum")[0].value
    cost2 = $("input#gold")[0].value
    cost3 = $("input#silver")[0].value
    $.post({
        url : "http://127.0.0.1:5000/api/seat/set",
        data : {
            platinum : cost1,
            gold : cost2,
            silver : cost3
        }

    });
    console.log(cost1)
    console.log(cost2)
    console.log(cost3)
}