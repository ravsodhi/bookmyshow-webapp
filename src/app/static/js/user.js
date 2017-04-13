$(document).ready(function(){
    $.ajax({
        url:'http://127.0.0.1:5000/api/user_info', 
        success: function(response){
        	user_name = response.info.name;
        	user_email = response.info.email;
            console.log(response)
        	document.getElementById('user_name').innerHTML = user_name;
        	document.getElementById('user_email').innerHTML = user_email;

        	$.ajax({
        		url: 'http://127.0.0.1:5000/api/booking/user', 
        		success: function(response){
        			array = response.booking_data;
        			str = "<tr class=\"trow\"><td class=\"tcol\">Title</td><td class=\"tcol\">Date</td>" + 
        			       "<td class=\"tcol\">Time</td><td class=\"tcol\">Hall Name</td><td class=\"tcol\">Hall Type</td>"
                           + "<td class=\"tcol\">Cost($)</td><td class=\"tcol\">Seats</td></tr>";
        			str2 = "";
        			for(var i = 0;i < array.length; i++)
        			{
        				str2 = "";
        				for(var j = 0;j < array[i].seats.length; j++)
        				{
        					if(j != array[i].seats.length - 1)
        						str2 += array[i].seats[j] + ',';
        					else
        						str2 += array[i].seats[j];

        				}
                        console.log(str2)
        				str += '<tr class=\"trow\"> <td class=\"tcol\">' + array[i].movie_title + '</td><td class=\"tcol\">'
        				+ array[i].screening_date + '</td><td class=\"tcol\">' + array[i].screening_time + '</td><td class=\"tcol\">'
        				+ array[i].audi_name + '</td><td class=\"tcol\">' + array[i].audi_type + '</td><td class=\"tcol\">'
        				+ array[i].cost + '</td><td class=\"tcol\">' + str2 + '</td>';
        			}
        			document.getElementById('booking_info').innerHTML = str;
        		}
        	});
		},
		error: function(response){
			console.log(response);
		}
    });
});
