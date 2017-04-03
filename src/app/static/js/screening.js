// works on load of screening.html
$(document).ready(function() {
            var array = [];
            var array2 = [];
            var movie_id = document.getElementsByClassName(movie_id_required)[0].innerHTML;
            $.ajax({
                url: "127.0.0.1:5000/api/screening/movies",
                data: "movie_id=" + movie_id,
                success: function(response) {
                    array = response.dates;
                },
                error: function(response) {
                    console.log('Error in fetching dates');
                }
            });
            var str = "";
            for (var i = 0; i < array.length; i++) {

                str += '<button class = \"button\" onclick = \'slot_fetch(\"' + array[i].date + '\", ' + movie_id + ');\' >' + array[i].date + '</button>';
            }

            $("div.btn-group").html(str);
        })
/*        var slot_fetch = function(date, movie_id) {
            $.ajax({
url:"127.0.0.1:5000/api/screening/date", 
data: "date_id=" + date + "&movie_id" + movie_id , 
success: function(response){
        array2 = response.slots;
        }, 
error: function(response){
        console.log('Error in fetching slots');
        }
        });
        
        var str2 = "";
 
        // Now we got audi's in ascending order of their lexicographical name and hence we can loop until a different audi is found or audi's list is finished.....
        // This is to be done today.....

*/
