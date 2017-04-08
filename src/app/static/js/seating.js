$(document).ready(
    function renderSeats() {
        arr = []
        var max_row = 9;
        s = window.location.pathname.split("/")[2]
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
                            max_row = 15;
                        else if (!ans.localeCompare("Medium"))
                            max_row = 12;
                        else if (!ans.localeCompare("Small"))
                            max_row = 8;
                        var str_full = "";

                        for (var i = max_row; i >= 0; i--) {
                            row_no = String.fromCharCode(65 + i);
                            var str_head = "<li class=\"row row-" + row_no + "\"><ol class=\"seats\" type=\"A\"><li class=\'seat\' style=\'color:white\'>" + row_no + "</li>";
                            var str_body = "";
                            for (var j = 0; j < 15; j++) {
                                column_no = j + 1;
                                for (var k = 0; k < arr.length;) {
                                    row = arr[k].seat_row;
                                    column = arr[k].seat_column;

                                    if (row == row_no && column == column_no) {
                                        str_body += "<li class=\"seat\"><input type=\"checkbox\" disabled id=\"" + row_no + column_no + "\" /><label for=\"" + row_no + column_no + "\">" + column_no + "</label></li>";
                                        break;
                                    } else {
                                        k++;
                                    }
                                }
                                if (k == arr.length)
                                    str_body += "<li class=\"seat\"><input type=\"checkbox\" id=\"" + row_no + column_no + "\" /><label for=\"" + row_no + column_no + "\">" + column_no + "</label></li>";

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
        //get audi type//
        //get data//

    }
);

function bookNow() {
    checked = $('input:checked');
    str = ""
    for (var i = 0; i < checked.length; i++) {
        if (i != checked.length - 1)
            str += checked[i].id + ","
        else
            str += checked[i].id
    }
    console.log(checked)
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
        }
    })

}
