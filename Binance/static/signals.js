
function getsig(){

            $.ajax({
            type: 'GET',
                url: "/getSignals",
                dataType: 'json',
            success: function (data) {


            if($('table#table1').length){

         var removeTab = document.getElementById('table1');
         var remove = document.getElementById('myPager');
        var parentEl = removeTab.parentElement;
       var parentPA = remove.parentElement;

        parentEl.removeChild(removeTab);
        parentPA.removeChild(remove)
            }

            var stock = new Array()
            var myTableDiv = document.getElementById("getsignals")

            var table = document.createElement('TABLE')
               table.id = "table1";
            var tableBody = document.createElement('TBODY')
            tableBody.id = "tbody";
            var tableHead = document.createElement('THEAD')


                     table.border = '1'
            table.appendChild(tableHead)
            table.appendChild(tableBody);

            var heading = new Array();
            heading[0] = "SignalID"
            heading[1] = "Signal Pips"
            heading[2] = "Signal Subscribers"
            heading[3] = "Signal Name"
            heading[4] = "Signal Currency"
            heading[5] = "Choose Signal"

            d = document.getElementById("symbol").value
            if(d.localeCompare("Choose the Currency")==0){
                d="all"
            }
            var j=0;
            for (var i = 0; i < data.length; i++){

            var val = data[i].currency.replace("\n","").replace(" ","")
            console.log(val)
            console.log(d)
            if(val.localeCompare("Signalcurrency"))
            if(!d.localeCompare("all")==0){
                if(d.localeCompare(val)==0){

                      stock[j]= new Array(data[i].id,data[i].pips,data[i].subs,data[i].name,data[i].currency);
                            j++;
                }}else{

                   stock[j]= new Array(data[i].id,data[i].pips,data[i].subs,data[i].name,data[i].currency);
                    j=j+1;
                }
           };
               console.log(j)

            //TABLE COLUMNS
            var tr = document.createElement('TR');
            tableBody.appendChild(tr);
            for (i = 0; i < heading.length; i++) {
                var th = document.createElement('TH')
                th.width = '75';
                th.appendChild(document.createTextNode(heading[i]));
                tr.appendChild(th);

            }

                  //TABLE ROWS
            for (i = 0; i < stock.length; i++) {
    var tr = document.createElement('TR');
    var nick="tr"+i
    tr.id = nick
    for (j = 0; j < stock[i].length; j++) {
        var td = document.createElement('TD')
        td.appendChild(document.createTextNode(stock[i][j]));
        tr.appendChild(td)
    }
            var td = document.createElement('TD')
         var aTag = document.createElement('a');
             aTag.setAttribute('href',"javascript:choose("+nick+")");
     aTag.innerHTML='<i class="fas fa-signal"></i>'
      td.appendChild(aTag)
              tr.appendChild(td)
    tableBody.appendChild(tr);
}

            myTableDiv.appendChild(table)
            var div = document.getElementById("pager")
            var ul = document.createElement('UL')
            ul.classList.add("pagination")
            ul.id = "myPager"
            div.appendChild(ul)


 $('#tbody').pageMe({
  pagerSelector:'#myPager',
  perPage: 15,
  hidePageNumbers: false
});
  }

  });
  }



$(document).ready(function(){
    getsig();

});



 function sortTable() {

          var remove = document.getElementById('myPager');
       var parentPA = remove.parentElement;
        parentPA.removeChild(remove)

 d = document.getElementById("sorder").value
 console.log(d)

  var table, rows, switching, i, x, y, shouldSwitch;
  table = document.getElementById("table1");
  switching = true;
  /*Make a loop that will continue until
  no switching has been done:*/
  while (switching) {
    //start by saying: no switching is done:
    switching = false;
    rows = table.rows;
    /*Loop through all table rows (except the
    first, which contains table headers):*/
    for (i = 1; i < (rows.length - 1); i++) {
      //start by saying there should be no switching:
      shouldSwitch = false;
      /*Get the two elements you want to compare,
      one from current row and one from the next:*/
      x = rows[i].getElementsByTagName("TD")[d];
      y = rows[i + 1].getElementsByTagName("TD")[d];
      //check if the two rows should switch place:
      if (Number(x.innerHTML) < Number(y.innerHTML)) {
        //if so, mark as a switch and break the loop:
        shouldSwitch = true;
        break;
      }
    }
    if (shouldSwitch) {
      /*If a switch has been marked, make the switch
      and mark that a switch has been done:*/
      rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
      switching = true;
    }
  }

            var div = document.getElementById("pager")
            var ul = document.createElement('UL')
            ul.classList.add("pagination")
            ul.id = "myPager"
            div.appendChild(ul)

   $('#tbody').pageMe({
  pagerSelector:'#myPager',
  perPage: 15,
  hidePageNumbers: false
});
}


function choose(par){
console.log(par)
var c = par.childNodes;

            data = {
             "code": c[0].innerHTML,

            }
            console.log(data)
            $.ajax({
                type: 'POST',
                contentType: 'application/json',
                data: JSON.stringify(data),
                dataType: 'json',
                url: 'http://127.0.0.1/csignal',
                success: function (e) {
                    console.log(e);
                },
                error: function(error) {
                console.log(error);
            }
            });
}



