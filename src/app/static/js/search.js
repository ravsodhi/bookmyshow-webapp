$(document).ready(function() {

var x = window.location.href;
        x =  x.split("/")
        x = x[0] + "//" + x[2] + "/" + "movie/" 
        $("#search").on("keyup",function () {
            $.ajax ({
                url : "/api/movies/search",
                method : "GET",
                data : {
                    query:$('#search').val()
                },
                success : function(resp){
                    console.log(resp.movies)
                    str=""
                    for(var i=0;i<resp.movies.length;i++)
                    {
                        str+="<tr style=\'width:392 px;\''><td><a href=\'" +  x +  resp.movies[i].id +"\'>" + resp.movies[i].title+"</a></td></tr>";
                    }
                    if(str !="")
                    $("#response").html(str);
                    else
                    $("#response").html("");

                }
            })
            // body...
        })
    })