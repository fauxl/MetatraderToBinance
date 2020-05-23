
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



function change(){
   $('form').animate({height: "toggle", opacity: "toggle"}, "slow"
);}

function gtfocus(){
$('.paragraph').focus();}

$('.message a').click(function(){
change();
gtfocus();
})

