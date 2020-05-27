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

        let dropdown = $('#symbol');

        dropdown.empty();

        dropdown.append('<option selected="true" disabled>Choose the Symbol</option>');
        dropdown.prop('selectedIndex', 0);


   $.ajax({

            type: 'GET',
            url: "/getTicket",
            dataType: 'json',
            success: function (data) {
            for(i =0; i<data.length;i++){
                        dropdown.append($('<option></option>').attr('value', data[i].price).text(data[i].symbol));
                    document.getElementById("cp").value = "Select value to see the current Price";
                            console.log(data[i].symbol)
             }}
  });
  })

function changeprice(){
          d = document.getElementById("symbol").value;
           document.getElementById("cp").value = d

}