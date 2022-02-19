$(function(){
    $("body").on("click", "#countryRadios [id]", function(){
        var $this = $(this),
                thisSelectedValue = $this.val();
        if (thisSelectedValue == 1){
            $("#dynmSelect").empty().append("<select name='city'><option value='cac1.html'>Country A City 1</option><option value='cac2.html'>Country A City 2</option><option value='cac3.html'>Country A City 3</option></select>");
        }else if (thisSelectedValue == 2){
            $("#dynmSelect").empty().append("<select name='city'><option value='cbc1.html'>Country B City 1</option><option value='cbc2.html'>Country B City 2</option><option value='cbc3.html'>Country B City 3</option></select>");
        }
    });
    $("body").on("click", "#submitSelect", function(e){
        e.preventDefault();
        var $this = $("#dynmSelect select").val();
        console.log($this);
        if ($this){
            document.location.href = $this;
        }else{
            $("#dynmSelect").text("You must first select a Country");
        }
    });
});
