$('.product_video').hover(function toggleControls() {
    if (this.hasAttribute("controls")) {
        this.removeAttribute("controls");
    } else {
        this.setAttribute("controls", "controls");
    }
});

$(function() {
        $(".dropdown").hover(
            function(){ $(this).addClass('open') },
            function(){ $(this).removeClass('open') }
        );
    });
  