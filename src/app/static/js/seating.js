var seating = function() {
    //    var t = [];
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
                cost += cost_obj.cost()
            else if (k > 7 && k < 12)
                cost += cost_obj.cost1()
            else
                cost += cost_obj.cost2()
        }
        str1 = "<h3 id=\"dyncost\" style=\"color:white\">Cost : " + cost + "</h3>"
        str2 = "<h3 id=\"dynseat\" style=\"color:white\">Selected Seats: " + seatsselected + "</h3>"

        $("h3#dyncost").html(str1);
        $("h3#dynseat").html(str2);
    }

    function bookNow() {
        checked = $('input:checked');
        if (checked.length == 0) {
            alert('Please select a seat to book!');
            return;
        }

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
            url: "/api/booking/add",
            data: {
                seats: str,
                scr_id: s,
            },
            success: function(response) {
                console.log(response)
                if (response.cheater) {
                    alert('Please select valid seats only!');
                }
                if (response.success) {

                    var x = window.location.href;
                    x = x.split("/")
                    x = x[0] + "//" + x[2] + "/" + "viewticket"
                    console.log(x);
                    //window.location.href = "http://127.0.0.1:5000/viewticket"
                    window.location.href = x

                } else //(!response.success)
                //                   window.location.href = "http://127.0.0.1:5000/login"
                {
                    var x = window.location.href;
                    x = x.split("/")
                    x = x[0] + "//" + x[2] + "/" + "login"
                    window.location.href = x

                }
            }
        });
    }
    var safe = {}
    safe.bookNow = bookNow
    safe.costdetector = costdetector
    return safe;

}();

var array_maker = function(a, b, c) {
    var t = [];
    t.push(a);
    t.push(b);
    t.push(c);
    var cost = function() {
        return t[0];
    }
    var cost1 = function() {
        return t[1];
    }
    var cost2 = function() {
        return t[2];
    }
    var object = {};
    object.cost = cost;
    object.cost1 = cost1;
    object.cost2 = cost2;
    return object;
}
var max_row_maker = function(max_row) {
	//Not needed, as the ajax call would have been completed till then and user can't alter anything in that.
    var row = max_row;
    var row1 = function() {
        return row;
    }
    var object = {};
    object.max_row = row1;
    return object;
}
$(document).ready(
    function renderSeats() {
        $.ajax({
            url: "/api/seat/get",
            success: function(response) {
                //           console.log(response.cost)
                //             seating.t.push(response.cost[0]);
                //            seating.t.push(response.cost[1]);
                //           seating.t.push(response.cost[2]);
                // This function can be used to make objects more safer
                cost_obj = array_maker(response.cost[0], response.cost[1], response.cost[2]);
                //           console.log(cost_obj);
                //cost will be an object loaded with other methods to retrieve costs

            }
        });

        //var max_row;
        arr = [];
        s = window.location.pathname.split("/")[2];
        $.ajax({
            //url: "http://127.0.0.1:5000/api/booking/" + s,
            url: "/api/booking/" + s,

            success: function(response) {
                arr = response.seats;
                $.post({
                    // url: "http://127.0.0.1:5000/api/screening/audi",
                    url: "/api/screening/audi",
                    data: {
                        scr_id: s
                    },
                    success: function(response) {
                        ans = response.ans;
                        if (!ans.localeCompare("Big"))
                            max_row = max_row_maker(14);
                        else if (!ans.localeCompare("Medium"))
                            max_row = max_row_maker(11);
                        else if (!ans.localeCompare("Small"))
                            max_row = max_row_maker(7);
                        var str_full = "";

                        if (max_row.max_row() == 14)
                            hall_decider = 2;
                        else if (max_row.max_row() == 11)
                            hall_decider = 1;
                        else
                            hall_decider = 0;

                        for (var i = max_row.max_row(); i >= 0; i--) {
                            row_no = String.fromCharCode(65 + i);
                            var str_head = "";

                            if (hall_decider == 2 && i == 14) {
                                str_head += "<h3 style=\"text-align:center;color:white \">Platinum Class (Rs." + cost_obj.cost2() + ")</h3>";
                            }
                            if ((hall_decider == 2 || hall_decider == 1) && i == 11)
                                str_head += "<h3 style=\"text-align:center; color:white\">Gold Class (Rs." + cost_obj.cost1() + ")</h3>"
                            if ((hall_decider == 2 || hall_decider == 1 || hall_decider == 0) && i == 7)
                                str_head += "<h3 style=\"text-align:center; color:white\">Silver Class (Rs." + cost_obj.cost() + ")</h3>"

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
                                    str_body += "<li class=\"seat\"><input type=\"checkbox\"" + "onclick = seating.costdetector(" + max_row.max_row() + ") id=\"" + row_no + column_no + "\"" + "/><label for=\"" + row_no + column_no + "\">" + column_no + "</label></li>";

                            }

                            str_full += str_head + str_body + "</ol></li>";
                            str_body = "";
                        }
                        // added so that user can's access arr array..
                        ans = [];

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
