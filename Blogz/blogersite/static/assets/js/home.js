$(document).ready(function () {

    $(".subs").on("click", function () {
        var userID = $(this).attr("userID");
        var catID = $(this).attr("catID");
        console.log(userID, catID)

//Subscribe

        if ($(this).html() == "Subscribe") {
            //change button to unsubscribe
            $(this).html("unsubscribe");
            $.ajax({

                url: 'subscribe/',
                type: 'POST',
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
                error: function (error) {
                    console.log('subs error')
                }
            });

        }
//UnSubscribe
        else {
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


    // $(".like").on("click", function () {
    //     // var user_ID = $(this).attr("user_ID");
    //     var post_ID = $(this).val();
    //     console.log(post_ID);
    //
    //
    //     $.ajax({
    //
    //         url: "like",
    //         type:"POST",
    //         data: {
    //             'post_ID': post_ID
    //         },
    //         dataType: 'json',
    //         success: function (data) {
    //             console.log("3aml like")
    //             console.log("succ"+data)
    //
    //         },
    //         error: function (error) {
    //             console.log(error)
    //         }
    //
    //
    //     });
    //
    // });


    $(".dislike").on("click", function () {
        var user_ID = $(this).attr("user_ID");
        var post_ID = $(this).attr("post_ID");
        console.log(user_ID, post_ID);


        $.ajax({
            url: 'dislike',
            type: 'POST',
            data: {
                'user_ID': user_ID,
                'post_ID': post_ID
            },
            dataType: 'json',
            success: function () {
                console.log("3amlt dislike :D")
            },
            error: function () {
                console.log("3andk error fel dislike")
            }


        });

    });


});