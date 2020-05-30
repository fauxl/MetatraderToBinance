
$(document).on('pagebeforeshow', '#formPage', function(){

$(document).on('click', '#submit', function() { // catch the form's submit event

    if($('#name').val().length > 0 && $('#email').val().length > 0 && $('#memory').val().length > 0){


        var that = $(this),
            contents = that.serialize();


        // Send data to server through ajax call
        // action is functionality we want to call and outputJSON is our data


        $.ajax({
            url: 'http://www....',
            dataType: 'json',
            type: 'post',
            data: contents,
            async: true,
            beforeSend: function() {
                // This callback function will trigger before data is sent
                $.mobile.showPageLoadingMsg(true); // This will show ajax spinner
            },
            complete: function() {
                // This callback function will trigger on data sent/received complete
                $.mobile.hidePageLoadingMsg(); // This will hide ajax spinner
            },

            success: function(data) {
                console.log(data);


            },
            error: function (request,error) {
                // This callback function will trigger on unsuccessful action
                alert('Network error has occurred please try again!');
            }
        });


    } else {
        alert('Please fill all nececery fields');
    }
    return false; // cancel original event to prevent form submitting
});
});


window.onscroll = function() {myFunction()};

var header = document.getElementById("myTopnav");
var sticky = header.offsetTop;

function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}

$(document).ready( function() {
var x = document.cookie;
var nav = document.getElementById("login");
var div = document.getElementById("drop");
var drop = document.getElementById("myDropdownn");

console.log(drop);

if (!x.substr("UserID")){
    nav.innerHTML= "Login/Registrazione";
    nav.setAttribute('href', "http://127.0.0.1/login");
   drop.style.visibility="hidden";
    nav.style.padding="2% 0% 2% 0% ";
    div.style.padding="2% 0% 2% 0% ";
    }
else{
   var cookievalue = x.replace("userID="," ");
   nav.innerHTML= cookievalue;
   drop.style.visibility="visible";
   nav.setAttribute('href', "http://127.0.0.1");
   nav.style.padding="2% 0% 2% 0%";
}

});

function change(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow"
);}


$('.message a').click(function(){
change();
})


var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
var currentScrollPos = window.pageYOffset;
  if (prevScrollpos > currentScrollPos) {
    document.getElementById("myTopnav").style.top = "-1px";
    document.getElementById("myTopnav").style.background = "#272e38";
        document.getElementById("myDropdownn").style.background = "#272e38";
        document.getElementById("myDropdown").style.background = "#272e38";


  } else {
    document.getElementById("myTopnav").style.top = "-110px";
  }
  if ( window.pageYOffset == 0) {
      document.getElementById("myTopnav").style.background = "transparent";
      document.getElementById("myDropdownn").style.background = "transparent";
        document.getElementById("myDropdown").style.background = "transparent";

  }
  prevScrollpos = currentScrollPos;
}
