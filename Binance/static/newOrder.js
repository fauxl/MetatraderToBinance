$(document).ready( function() {
        $('#contact-submit').click(function() {
           var formdata = $('#contact').serialize();
           $.ajax({
                 type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(formdata),
                dataType: 'json',
                url: 'http://127.0.0.1/insert',
                success: function (e) {
                    console.log(e);
                },
                error: function(error) {
                console.log(error);
            }
            });
        });
  });