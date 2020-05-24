$(document).ready( function() {
        $('#contact-submit').click(function() {
           var formdata = $('#contact').serialize();
        if($('#symbol').val().length > 0 && $('#volume').val().length > 0 && $('#tipo').val().length > 0){

            data = {
                "simbolo": $('#symbol').val(),
                "volume":  $('#volume').val(),
                "tipo": $('#tipo').val(),
                "SL": $('#sl').val(),
                "TP":$('#tp').val()
            }
           $.ajax({
                 type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data),
                dataType: 'json',
                url: 'http://127.0.0.1/insert',
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

$(document).ready(function(){
   $.ajax({
            type: 'GET',
                url: "/insert",
                dataType: 'json',
            success: function (data) {
                            console.log("prova")

                console.log(JSON.stringify(data))
               },
                error: function(error) {
                console.log(error);}
  });
  })