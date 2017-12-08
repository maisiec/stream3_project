$(document).ready(function(){
  $("#nav-toggle a").click(function(event){
    $("#main-nav").toggleClass("active");
    $("#nav-toggle a").toggleClass("active");
    event.preventDefault();
  });
}); 

jQuery(function($) {
    $(window).scroll(function() {
        var scrollPos = $(window).scrollTop();
        var navOpacity = scrollPos / 100;

        $('.navbar').css("opacity", navOpacity);

        if ($('nav').css('opacity') < 1) {
            $('.navbar').css('opacity', 1);
        }
    });
});