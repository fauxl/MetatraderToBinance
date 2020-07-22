function getdata(){

            $.ajax({
            type: 'GET',
                url: "/getdata",
                dataType: 'json',
            success: function (data) {
         if($('table#table1').length){

        var removeTab = document.getElementById('table1');
         var removeTit = document.getElementById('metitle');
        var parentEl = removeTab.parentElement;
        parentEl.removeChild(removeTab);
         parentEl.removeChild(removeTit)

            }
                        var stock = new Array()
            var myTableDiv = document.getElementById("metatrader")

            var table = document.createElement('TABLE')
            var title = document.createElement('H2')
            var t = document.createTextNode("Your Order History in Metatrader");
            // Create a text node

               table.id = "table1";
               title.id = "metitle"

            var tableBody = document.createElement('TBODY')
            tableBody.id = "tbody";
            var tableHead = document.createElement('THEAD')


                   table.border = '1'
            table.appendChild(tableHead)
            table.appendChild(tableBody);
            title.appendChild(t)
            myTableDiv.appendChild(title)


            var heading = new Array();
            heading[0] = "Ticket"
            heading[1] = "Type Operation"
            heading[2] = "Symbol"
            heading[3] = "Stop Loss"
            heading[4] = "Take Profit"
            heading[5] = "Order Opening"
            heading[6] = "Close Price"
            heading[7] = "Quantity"
            heading[8] = "Profit"
            console.log(data)

          var j=0;
            for (var i = 0; i < data.length; i++){
            var p = data[i][7];

                if(p.localeCompare('Closed')==0){
                      stock[j]= new Array(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][8],data[i][9]);
                            j++;
                }

                console.log(stock.length)

           } //TABLE COLUMNS
            var tr = document.createElement('TR');
            tableHead.appendChild(tr);
            for (i = 0; i < heading.length; i++) {
                var th = document.createElement('TH')
                th.width = '75';
                th.appendChild(document.createTextNode(heading[i]));
                tr.appendChild(th);

            }

                  //TABLE ROWS
            for (i = 0; i < stock.length; i++) {
    var tr = document.createElement('TR');
    for (j = 0; j < stock[i].length; j++) {
        var td = document.createElement('TD')
        td.appendChild(document.createTextNode(stock[i][j]));
        tr.appendChild(td)
    }
    tableBody.appendChild(tr);
}

            myTableDiv.appendChild(table)

$('#tbody').pageMe({
  pagerSelector:'#myPager',
  perPage: 3,
  hidePageNumbers: false
});



  }

  });
  }

function getBinancedata(){

            $.ajax({
            type: 'GET',
                url: "/getdata",
                dataType: 'json',
            success: function (data) {
         if($('table#table2').length){


         var removeTab = document.getElementById('table2');
         var removeTit = document.getElementById('bintitle');
        var parentEl = removeTab.parentElement;
        parentEl.removeChild(removeTab);
         parentEl.removeChild(removeTit)

            }
                        var stock = new Array()
            var myTableDiv = document.getElementById("binance")

            var table = document.createElement('TABLE')
             var title = document.createElement('H2')
            var t = document.createTextNode("Your Order History in Binance");
            // Create a text node
               table.id = "table2";
               title.id = "bintitle";

            var tableBody = document.createElement('TBODY')
               tableBody.id = "tbodyb";
            var tableHead = document.createElement('THEAD')


                     table.border = '1'
            table.appendChild(tableHead)
            table.appendChild(tableBody);
            title.appendChild(t)
            myTableDiv.appendChild(title)



            var heading = new Array();
            heading[0] = "Ticket"
            heading[1] = "Type Operation"
            heading[2] = "Symbol"
            heading[3] = "Stop Loss"
            heading[4] = "Take Profit"
            heading[5] = "Order Opening"
            heading[6] = "Close Price"
            heading[7] = "Quantity"
            heading[8] = "Profit"

            var j=0;
            for (var i = 0; i < data.length; i++){
            var p = data[i][7];

                if(p.localeCompare('Closed')==0){
                      stock[j]= new Array(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4],data[i][5],data[i][6],data[i][8],data[i][9]);
                            j++;
                }

                console.log(stock.length)

           } //TABLE COLUMNS
            var tr = document.createElement('TR');
            tableHead.appendChild(tr);
            for (i = 0; i < heading.length; i++) {
                var th = document.createElement('TH')
                th.width = '75';
                th.appendChild(document.createTextNode(heading[i]));
                tr.appendChild(th);

            }

                  //TABLE ROWS
            for (i = 0; i < stock.length; i++) {
    var tr = document.createElement('TR');
    for (j = 0; j < stock[i].length; j++) {
        var td = document.createElement('TD')
        td.appendChild(document.createTextNode(stock[i][j]));
        tr.appendChild(td)
    }
    tableBody.appendChild(tr);
}

            myTableDiv.appendChild(table)

  $('#tbodyb').pageMe({
  pagerSelector:'#myPagerb',
  perPage: 3,
  hidePageNumbers: false
});

  }


  });
  }



function double(){
    getdata();
    getBinancedata();

}


$(document).ready(function(){

var x = document.cookie;
if (!x.substr("UserID")){
var mt = document.getElementById('metatrader');
var bi = document.getElementById('binance');
 var parentElM = mt.parentElement;
  var parentElB = bi.parentElement;
        parentElM.removeChild(mt);
        parentElB.removeChild(bi);
}else{
var ab = document.getElementById('about');
 var parentEl = ab.parentElement;
        parentEl.removeChild(ab);
   double();

}

});


