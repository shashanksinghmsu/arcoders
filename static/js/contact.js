$(".contactForm").submit(function (e) {
    var form = this;
    e.preventDefault();
    setTimeout(function () {
        form.submit()
    }, 1200)

})
$(".neon").mouseover(function () {
    $(".neon").css("color", "#122647");
});
$(".neon").mouseout(function () {
    $(".neon").css("color", "dodgerblue");
});
