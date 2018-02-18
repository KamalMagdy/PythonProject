$(document).ready(function(){

	$(".subs").on("click",function () {
		var userID=$(this).attr("userID");
		var catID=$(this).attr("catID");
		console.log(userID,catID)

//Subscribe

	if($(this).html()=="Subscribe"){
		//change button to unsubscribe
		$(this).html("unsubscribe");
		$.ajax({

        url: 'subscribe/',
        type: 'GET',
        data: {
          'userID': userID,
          'catID': catID
        },

        dataType: 'json',
        success: function (data) {
          if (data.success) {
          	console.log("user subscribed in catagory");

          }

        },
            error: function(error){
            console.log('subs error')
            }
      });

	}
//UnSubscribe
	else{
		$(this).html("Subscribe");
		$.ajax({
        url: 'unsubscribe/',
        type: 'POST',
        data: {
          'userID': userID,
          'catID': catID
        },

        dataType: 'json',
        success: function (data) {
          if (data.success) {
          	console.log("user unsubscribed in catagory");

          }
        }
      });
	}
	});
});