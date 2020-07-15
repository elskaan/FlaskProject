$(function () {
    $(".skill_progress span").each(function () {
        $(this).animate({
            "width": $(this).data("width")
        }, 5000)
    })
})