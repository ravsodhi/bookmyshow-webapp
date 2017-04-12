var max_row;
var t = [];

$(document).ready(
    function renderSeats() {
        $.ajax({
            url: "http://127.0.0.1:5000/api/seat/get",
            success: function(response) {
                //           console.log(response.cost)
                t.push(response.cost[0]);
                t.push(response.cost[1]);
                t.push(response.cost[2]);
                    //         console.log(t);

            }
        });


        arr = [];
        s = window.location.pathname.split("/")[2];
        $.ajax({
            url: "http://127.0.0.1:5000/api/booking/" + s,
            success: function(response) {
                arr = response.seats;
                $.post({
                    url: "http://127.0.0.1:5000/api/screening/audi",
                    data: {
                        scr_id: s
                    },
                    success: function(response) {
                        ans = response.ans;
                        if (!ans.localeCompare("Big"))
                            max_row = 14;
                        else if (!ans.localeCompare("Medium"))
                            max_row = 11;
                        else if (!ans.localeCompare("Small"))
                            max_row = 8;
                        var str_full = "";

                        if (max_row == 14)
                            hall_decider = 2;
                        else if (max_row == 11)
                            hall_decider = 1;
                        else
                            hall_decider = 0;

                        for (var i = max_row; i >= 0; i--) {
                            row_no = String.fromCharCode(65 + i);
                            var str_head = "";

                            if (hall_decider == 2 && i == 14) {
                                str_head += "<h3 style=\"text-align:center;color:white \">Platinum Class (Rs." + t[2] + ")</h3>";
                            }
                            if ((hall_decider == 2 || hall_decider == 1) && i == 11)
                                str_head += "<h3 style=\"text-align:center; color:white\">Gold Class (Rs." + t[1] + ")</h3>"
                            if ((hall_decider == 2 || hall_decider == 1 || hall_decider == 0) && i == 7)
                                str_head += "<h3 style=\"text-align:center; color:white\">Silver Class (Rs." + t[0] + ")</h3>"

                            str_head += "<li class=\"row row-" + row_no + "\"><ol class=\"seats\" type=\"A\"><li class=\'seat\' style=\'color:white\'>" + row_no + "</li>";
                            var str_body = "";

                            for (var j = 0; j < 15; j++) {
                                column_no = j + 1;
                                for (var k = 0; k < arr.length;) {
                                    row = arr[k].seat_row;
                                    column = arr[k].seat_column;

                                    if (row == row_no && column == column_no) {
                                        str_body += "<li class=\"seat\"><input type=\"checkbox\" disabled id=\"" + row_no + column_no + "\"" + "/><label for=\"" + row_no + column_no + "\">" + column_no + "</label></li>";
                                        break;
                                    } else {
                                        k++;
                                    }
                                }
                                if (k == arr.length)
                                    str_body += "<li class=\"seat\"><input type=\"checkbox\"" + "onclick = costdetector(" + max_row + ") id=\"" + row_no + column_no + "\"" + "/><label for=\"" + row_no + column_no + "\">" + column_no + "</label></li>";

                            }

                            str_full += str_head + str_body + "</ol></li>";
                            str_body = "";
                        }

                        $("ol#seat-selector").html(str_full);


                    },
                    error: function(response) {
                        console.log("booking is not functional")
                    }
                });
            },
            error: function(response) {
                console.log("booking is not functional")
            }
        });



    }
);

var costdetector = function(max_row) {
    checked = $('input:checked');
    check_array = []
    for (var i = 0; i < checked.length; i++) {
        check_array.push(checked[i].id)

    }
    seatsselected = checked.length
    var cost = 0;
    for (var i = 0; i < check_array.length; i++) {
        k = check_array[i].charCodeAt(0) - 65
        if (k > -1 && k < 8)
            cost += t[0]
        else if (k > 7 && k < 12)
            cost += t[1]
        else
            cost += t[2]
    }
    str1 = "<h3 id=\"dyncost\" style=\"color:white\">Cost : " + cost + "</h3>"
    str2 = "<h3 id=\"dynseat\" style=\"color:white\">Selected Seats: " + seatsselected + "</h3>"

    $("h3#dyncost").html(str1);
    $("h3#dynseat").html(str2);




}

function bookNow() {
    checked = $('input:checked');
    str = ""
    for (var i = 0; i < checked.length; i++) {
        if (i != checked.length - 1)
            str += checked[i].id + ","
        else
            str += checked[i].id
    }
    console.log(checked);
    console.log(str)
    s = parseInt(window.location.pathname.split("/")[2])
    $.ajax({
        url: "http://127.0.0.1:5000/api/booking/add",
        data: {
            seats: str,
            scr_id: s,
        },
        success: function(response) {
            console.log(response)
            if(response.success)
             {

                window.location.href = "http://127.0.0.1:5000/viewticket"

                 }

            else//(!response.success)
                window.location.href = "http://127.0.0.1:5000/login"
                
        }
    });


}
