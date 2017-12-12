$(document).ready(function(){
  $("#nav-toggle a").click(function(event){
    $("#main-nav").toggleClass("active");
    $("#nav-toggle a").toggleClass("active");
    event.preventDefault();
  });
}); 

