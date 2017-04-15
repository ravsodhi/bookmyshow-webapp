
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
            $("select#selecthall").html(str);
        },
        error: function(response) {
            console.log("Error in fetching auditoriums")

        }
    })
     $.ajax({
        url: "http://127.0.0.1:5000/api/movies",
        success: function(response) {
            console.log(response.audi)
            movies = response.allmovies;
            str = ""
            for (var i = 0; i < movies.length; i++) {
                str += "<option value=\"" + movies[i].id + "\">" + movies[i].title + "</option>";
            }
            console.log(str)
            $("select#selectmovie").html(str);
        },
        error: function(response) {
            console.log("Error in fetching movies")

        }
    })
})


