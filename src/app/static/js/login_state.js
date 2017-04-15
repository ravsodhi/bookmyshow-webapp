    var valchecker = function()
    {
        $.post({
            url: 'http://127.0.0.1:5000/api/helper',
            success : function(response)
            {
               // console.log(response)
                //alert(response)
                if(response.success)
                window.location.href = 'http://127.0.0.1:5000/user/history';
                else
                window.location.href = 'http://127.0.0.1:5000/register';

            },
            error : function(response){
                console.log("Error")
            }

        });
    }
    var logchecker = function()
    {
         $.post({
            url: 'http://127.0.0.1:5000/api/helper',
            success : function(response)
            {
                //console.log(response)
                //alert(response)
                if(response.success)
                window.location.href = 'http://127.0.0.1:5000/logout';
                else
                window.location.href = 'http://127.0.0.1:5000/login';

                
            },
            error : function(response){
                console.log("Error")
            }

        });
    }