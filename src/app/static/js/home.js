var homer = (function () {
	var check = function(){
		$.post({
            url: '/api/todo',
            success: function (response) {
            	console.log(response)
            	if(response.success)
            	{
            		$.get({
            			url: 'api/movies',
            			dataType : 'html',
            			success : function(response){
            				console.log(response)
            				var k = response.replace('<li><a href="http://127.0.0.1:5000/register"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>'
                                ,'<li><span></span></li>')
                            var l = k.replace('<li><a href="http://127.0.0.1:5000/login"><span class="glyphicon glyphicon-log-in"></span> Login</a></li>','<li><a href="http://127.0.0.1:5000/logout"><span class="glyphicon glyphicon-log-in"></span> Log Out</a></li>')
                            console.log(l)
                            document.write(l)
            			},
            		});
    				
            	}
                

            },
        });
	
}
	 var aManager = {};
    aManager.check = check;
    return aManager;
	// body...
})();
