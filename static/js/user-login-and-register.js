var detailstabLinks = document.querySelectorAll(".detailstablinks");
var detailstabContent = document.querySelectorAll(".detailstabcontent");


detailstabLinks.forEach(function(el) {
    el.addEventListener("click", detailsopenTabs);
});


function detailsopenTabs(el) {
    var detailsbtnTarget = el.currentTarget;
    var detailsvaluetxt = detailsbtnTarget.dataset.valuetxt;

    detailstabContent.forEach(function(el) {
        el.classList.remove("detailsactive");
    });

    detailstabLinks.forEach(function(el) {
        el.classList.remove("detailsactive");
    });

    document.querySelector("#" + detailsvaluetxt).classList.add("detailsactive");

    detailsbtnTarget.classList.add("detailsactive");
}