    var valchecker = function()
    {
        $.post({
            url: '/api/helper',
            success : function(response)
            {
               // console.log(response)
                //alert(response)
                if(response.success)
                {
                    var x = window.location.href;
                    x = x.split("/")
                    x = x[0] + "//" + x[2] + "/" + "user/history"
                    window.location.href = x;

                }
                else
                {
                    var x = window.location.href;
                    x = x.split("/")
                    x = x[0] + "//" + x[2] + "/" + "register"
                    window.location.href = x;

                }

            },
            error : function(response){
                console.log("Error")
            }

        });
    }
    var logchecker = function()
    {
         $.post({
            url: '/api/helper',
            success : function(response)
            {
                //console.log(response)
                //alert(response)
                if(response.success)
                {
                    var x = window.location.href;
                    x = x.split("/")
                    x = x[0] + "//" + x[2] + "/" + "logout"
                    window.location.href = x;
                }
                else
                {
                    var x = window.location.href;
                    x = x.split("/")
                    x = x[0] + "//" + x[2] + "/" + "login"
                    window.location.href = x;
                }
                
            },
            error : function(response){
                console.log("Error")
            }

        });
    }