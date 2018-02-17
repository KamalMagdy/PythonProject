$(document).ready(function(){


alert("button was clicked.");
$(".subs").click(function(){
    var userID=$(this).attr("uid");
		var catID=$(this).attr("cid");
    console.log(userID,catID);
});
});