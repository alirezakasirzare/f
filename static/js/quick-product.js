function quick(n) {

    var i;
    var quickPage = document.getElementsByClassName("quick-product");
    var background = document.getElementsByClassName("background");
    for (i = 0; i < quickPage.length; i++) {
        quickPage[i].style.display = "none";
    }
    if (n != 0) {
        quickPage[n - 1].style.display = "block";
        background[0].style.display = "block";
    }
    if (n == 0) {
        background[0].style.display = "none";
    }
}