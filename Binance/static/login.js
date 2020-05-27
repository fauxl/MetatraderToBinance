$(document).ready( function() {
        $('#log').click(function() {
           var formdata = $('#enter').serialize();

        if($('#username').val().length > 0 && $('#pass').val().length > 0 ){
            data = {
                "username": $('#username').val(),
                "password":  $('#pass').val()
            }
           $.ajax({
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data),
                dataType: 'json',
                url: 'http://127.0.0.1/login',
                success: function (e) {
                    console.log(e);
                },
                error: function(error) {
                console.log(error);
            }
            });
             }  else {
        alert('Please fill all nececery fields');
    }
        });

  });


  $(document).ready( function() {
        $('#reg').click(function() {
           var formdata = $('#enter').serialize();

        if($('#name').val().length > 0 && $('#password').val().length > 0 && $('#email').val().length > 0 ){
            data = {
                "username": $('#name').val(),
                "password":  $('#password').val(),
                "email":  $('#email').val()
            }
           $.ajax({
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data),
                dataType: 'json',
                url: 'http://127.0.0.1/register',
                success: function (e) {
                    console.log(e);
                },
                error: function(error) {
                console.log(error);
            }
            });
             }  else {
        alert('Please fill all nececery fields');
    }
        });

  });