$(".cat-link").on("click", function (){
    // let img = $(".cat1").css('background-image').slice(26, -2)
    let catname = (this).find(".cat-name").html
    let h1 = $("#id > h1").first()
    if(h1.length>0) {
        h1.html(catname)
    }else {
        let header = $("<h1/>").addClass("text-muted mt-3").html(catname)
        header.prependTo("#id")
    }

    $ajax({
        method: 'get',
        url: '/uz/cat-ajax/' + catid + "/",
        success: function(result){
            $("#id > h1").nextAll().remove()

            $("")

        }
    })

    return false;
})
