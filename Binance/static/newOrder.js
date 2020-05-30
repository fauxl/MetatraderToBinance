
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