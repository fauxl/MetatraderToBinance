$(document).ready(function(){


   $.ajax({

            type: 'GET',
            url: "/getuserdata",
            dataType: 'json',
            success: function (data) {
            console.log(data)
             document.getElementById("username").value = data.user
             document.getElementById("password").value = data.password
              document.getElementById("email").value = data.mail
             document.getElementById("key").value = data.key
              document.getElementById("skey").value = data.skey
             document.getElementById("an").value = data.name
              document.getElementById("ac").value = data.id
             document.getElementById("ab").value = data.balance

                }
  });
  })