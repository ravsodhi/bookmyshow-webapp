function tempAlert(msg,duration)
{

  var el = document.createElement("div");
  el.innerHTML = msg;
  el.setAttribute("style","position:fixed ; top:87% ;bottom:5%; left:45% ; background-color:black ; height:9%;padding: 12px 20px;color:white;");
  setTimeout(function(){
  el.parentNode.removeChild(el);
 },duration);
 document.body.appendChild(el);
}

var authManager = (function() {
    var loginState = null;
    var intendedPath = null;

    var loggedIn = function (user) {
        loginState = {};
        loginState.loggedIn = true;
        loginState.user = user;
        page(intendedPath ? intendedPath : '/');
    };

    var showLogin = function() {
        viewManager.render('login', function ($view) {
            $view
                .find('form')
                .submitViaAjax(function (response) {
                    if (response.success) {
                        loggedIn(response.user);
                    } else {
                        if(response.message == "Email is not registered")
			            {
                            tempAlert("Email is not registered",3000);
                            document.forms[0].elements[0].value = ""
                            document.forms[0].elements[1].value = ""
                        }
                        if(response.message == "Wrong Password")
                        {
                            tempAlert("Wrong Password",3000);
                            document.forms[0].elements[1].value = ""

                        }
                    }
                });
        });
    };

    var logout = function () {
        $.post({
            url: '/api/logout',
            success: function (response) {
                loginState = null;
                page("/");
            },
        });
    }

    var showRegister = function () {
        viewManager.render('register', function ($view) {
            $view
                .find('form')
                .submitViaAjax(function (registerResponse) {
                    var form = this;
                    if (registerResponse.success) {
                        $.post({
                            url: '/api/login',
                            data: {
                                email: form.email.value,
                                password: form.password.value,
                            },
                            success: function(response) {
                                if (response.success) {
                                    loggedIn(response.user);
                                } else {
                                    path('/login');
                                }
                            },
                        })
                    } else {
                        console.log(registerResponse)
                        if (registerResponse.message == "Password's don't match")
                            {
                                tempAlert("Password's don't match",3000);
                               document.forms[0].elements[2].value = ""
                                document.forms[0].elements[3].value = ""
                            }
                        else if(registerResponse.message == "Please enter a valid email")
                        {
                                tempAlert("Please enter a valid email",3000);
                                document.forms[0].elements[3].value = ""
                        }
                        if(registerResponse.message == "Email is already registered")
                        {
                                tempAlert("Email is already registered",3000);
                                document.forms[0].elements[1].value = ""
                                document.forms[0].elements[2].value = ""
                                document.forms[0].elements[3].value = ""


                        }   
                        
                    }
                });
        });
    };

    var getLoginState = function (cb) {
        if (loginState === null) {
            $.get({
                url: '/api/login',
                success: function (response) {
                    loginState = {};
                    if (response.success) {
                        loginState.loggedIn = true;
                        loginState.user = response.user;
                    } else {
                        loginState.loggedIn = false;
                    }
                    cb(loginState);
                },
                error: function (response) {
                    cb(loginState);
                }
            });
        } else {
            cb(loginState);
        }
    };

    var requiresAuthentication = function(ctx, next) {
        getLoginState(function (state) {
            console.log(state);
            if (state && state.loggedIn) {
                window.location.href = "http://127.0.0.1:5000/home";
            } else {
                console.log("load")
                intendedPath = ctx.path;
                //showLogin();
                page('/login');
            }
        });
    };

    var allowOnlyGuest = function (ctx, next) {
        getLoginState(function (state) {
            if (state.loggedIn) {
                page('/');
            } else {
                next();
            }
        });
    };

    var aManager = {};
    aManager.showLogin = showLogin;
    aManager.logout = logout;
    aManager.showRegister = showRegister;
    aManager.allowOnlyGuest = allowOnlyGuest;
    aManager.requiresAuthentication = requiresAuthentication;
    return aManager;
})(); // function is called here only as there is only instance of it
