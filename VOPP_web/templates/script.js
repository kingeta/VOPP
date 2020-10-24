var ENTER_KEY = 13;

$(document).on('keypress', function(e) {
    console.log("javaisup");
  var code = e.keyCode || e.which
  if (code == ENTER_KEY) {
    var itemString = document.getElementById('bar_input').value;
    console.log("hello")
 //   $("#bar_submit").trigger("click");

    check(itemString)
    
  }
});

function check(itemString) {
    console.log("ere");
    console.log(itemString)
    if(document.getElementById(itemString)!== null){
        console.log("hello!!")
        document.getElementById(itemString).checked = true;
    }
    else{

    }
    return true;
}