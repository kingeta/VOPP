var ENTER_KEY = 13;

$(document).on('keypress', function(e) {
  var code = e.keyCode || e.which
  if (code == ENTER_KEY) {
    var itemString = document.getElementById('bar_input').value;
    console.log(itemString);
    document.getElementById('bar_input').value = '';
    check(itemString) 
    
  }
});

function check(itemString) {
    console.log(itemString)
    if(document.getElementById(itemString)!== null){
        document.getElementById(itemString).checked = true;
        document.getElementById(itemString).id = "checked";

    }
    else{
        alert("Item not in order!\nPress Enter to close")
    }

    return true;
}