$(function() {
    $('#btnSignUp').click(function() {
 
        $.post({
            url: '/api/register',
//            data: $('form').serialize(),
             data: {
                                email: form.email.value,
                                password: form.password.value,
                            },

            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});