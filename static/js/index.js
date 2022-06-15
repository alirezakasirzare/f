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

// function resMenuMobile (){
//     var toggeler = document.getElementById("menu-list").style.display
//     if (toggeler == "block") document.getElementById("menu-list").style.display = "none";
//     if (toggeler == "none") document.getElementById("menu-list").style.display = "block";

// }
// function resMenuTablet(){

// }
function menufunc() {
  var toggeler = document.getElementById('menu-list').style.display;

  // var mediaQuery = window.matchMedia("(max-width: 600px)")
  var mediaQuery2 = window.matchMedia('(max-width:900px)');
  if (mediaQuery2.matches) {
    if (toggeler == 'block')
      document.getElementById('menu-list').style.display = 'none';
    if (toggeler == 'none')
      document.getElementById('menu-list').style.display = 'block';
  } else {
    if (toggeler == 'none')
      document.getElementById('menu-list').style.display = 'flex';
    if (toggeler == 'flex')
      document.getElementById('menu-list').style.display = 'none';
  }

  // if (mediaQuery.matches) resMenuMobile()

  //   else{
  // if (toggeler == "none") document.getElementById("menu-list").style.display = "flex";
  // if (toggeler == "flex") document.getElementById("menu-list").style.display = "none";
  //   }
}
window.addEventListener('resize', function () {
  var toggeler = document.getElementById('menu-list').style.display;

  // var mediaQuery = window.matchMedia("(max-width: 600px)")
  if (toggeler == 'block')
    document.getElementById('menu-list').style.display = 'none';
  if (toggeler == 'flex')
    document.getElementById('menu-list').style.display = 'none';

  //   else {
  //     if (toggeler == "none") document.getElementById("menu-list").style.display = "flex";
  //     if (toggeler == "flex") document.getElementById("menu-list").style.display = "none";
  //       }
});

// =====================Responsive Menu===========
function myResFunction() {
  var x = document.getElementById('myTopnav');
  if (x.className === 'topnav') {
    x.className += ' responsive';
  } else {
    x.className = 'topnav';
  }
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
//=============================================== sliders ==========================================

var elms = document.getElementsByClassName('splide');
for (var i = 0; i < elms.length; i++) {
  new Splide(elms[i], {
    perPage: 3,
    perMove: 1,
    breakpoints: {
      768: {
        perPage: 1,
      },
      1024: {
        perPage: 2,
      },
    },
  }).mount();
}

//===========================slider=========================
var slideIndex = 1;
showSliders(slideIndex);

// dot-btn => image controls
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
    if (dotsBtn[slideIndex - 1]) {
      dotsBtn[slideIndex - 1].classList.add('slide-active');
    }
  }
}

setInterval(function () {
  showSliders((slideIndex = slideIndex + 1));
}, 3000);

//===================================== sliders =========================
