function message(type,msg) {
    var succ = type
    var messageText = msg
    var snackbar = document.getElementById('snackbar')

    if(succ == "sucsses"){
        snackbar.innerText = messageText
        snackbar.className += " sucsses"
    setTimeout(function(){
        snackbar.innerText = " "
         snackbar.classList.remove("sucsses")
        }, 3000);
}

if(succ == "error"){
    snackbar.innerText = msg
    snackbar.className += " error"
setTimeout(function(){
    snackbar.innerText = " "
     snackbar.classList.remove("error")
    }, 3000);
}

    // setTimeout(function(){ snackbar.classList.remove("error")}, 3000);
  }