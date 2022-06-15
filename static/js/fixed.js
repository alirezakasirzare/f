// ======================MENU=====================

var tabLinks = document.querySelectorAll('.tablinks');
var tabContent = document.querySelectorAll('.tabcontent');

tabLinks.forEach(function (el) {
  el.addEventListener('click', openTabs);
});

function openTabs(el) {
  var btnTarget = el.currentTarget;
  var valuetxt = btnTarget.dataset.valuetxt;

  tabContent.forEach(function (el) {
    el.classList.remove('active');
  });

  tabLinks.forEach(function (el) {
    el.classList.remove('active');
  });

  document.querySelector('#' + valuetxt).classList.add('active');

  btnTarget.classList.add('active');
}

function menufunc() {
  var toggeler = document.getElementById('menu-list').style.display;
  if (toggeler == 'none')
    document.getElementById('menu-list').style.display = 'flex';
  if (toggeler == 'flex')
    document.getElementById('menu-list').style.display = 'none';
}
// ======================MENU=====================
// ======================SEARCH_MENU==============
function myFunction() {
  document.getElementById('search-box').style.display = 'block';
}

function myFunction2() {
  document.getElementById('search-box').style.display = 'none';
}
// ======================SEARCH_MENU==============
//===========================slider=========================
var slideIndex = 1;
showSliders(slideIndex);

//dot-btn => image controls
function currentSlide(n) {
  showSliders((slideIndex = n));
}

function showSliders(n) {
  var i;
  var slides = document.getElementsByClassName('carousel-item');
  var dotsBtn = document.getElementsByClassName('dot-btn');
  if (slides.length) {
    if (n > slides.length) {
      slideIndex = 1;
    }
    if (n < 1) {
      slideIndex = slides.length;
    }
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = 'none';
    }
    for (i = 0; i < dotsBtn.length; i++) {
      dotsBtn[i].classList.remove('slide-active');
    }
    slides[slideIndex - 1].style.display = 'block';
    dotsBtn[slideIndex - 1].classList.add('slide-active');
  }
}

setInterval(function () {
  showSliders((slideIndex = slideIndex + 1));
}, 3000);

//===================================== sliders =========================
