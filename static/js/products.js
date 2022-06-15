//=========================== slider main product page ==================
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

//================================================  colors ==============================================
function colorSelector(n) {
  var i;
  var colorBox = document.getElementsByClassName('colors');
  for (i = 0; i < colorBox.length; i++) {
    colorBox[i].style.display = 'none';
  }
  colorBox[n - 1].style.display = 'block';
}

//======================================== change page horiz ==============================================

var pagenumber = 1;
pagechenger(pagenumber);

function pluspage(n) {
  pagechenger((pagenumber += n));
}

function pageslide(n) {
  pagechenger((pagenumber = n));
}

function pagechenger(n) {
  var i;
  var page = document.getElementsByClassName('products-page');

  var number = document.getElementsByClassName('page');
  if (n > page.length) {
    pagenumber = 1;
  }
  if (n < 1) {
    pagenumber = page.length;
  }
  for (i = 0; i < page.length; i++) {
    page[i].style.display = 'none';
  }
  for (i = 0; i < number.length; i++) {
    number[i].classList.remove('pageActive');
  }
  if (page[pagenumber - 1]) {
    page[pagenumber - 1].style.display = 'block';
  }
  if (number[pagenumber - 1]) {
    number[pagenumber - 1].classList.add('pageActive');
  }
}

//============================== change page vert ================
var pagenumber8 = 1;
pagechengers(pagenumber8);

function pluspages(n) {
  pagechengers((pagenumber8 += n));
}

function pageslides(n) {
  pagechengers((pagenumber8 = n));
}

function pagechengers(n) {
  var i;
  var pageVert = document.getElementsByClassName('products-page1');

  var number1 = document.getElementsByClassName('pages');
  if (n > pageVert.length) {
    pagenumber8 = 1;
  }
  if (n < 1) {
    pagenumber8 = pageVert.length;
  }
  for (i = 0; i < pageVert.length; i++) {
    pageVert[i].style.display = 'none';
  }
  for (i = 0; i < number1.length; i++) {
    number1[i].classList.remove('pageActive');
  }

  if (pageVert[pagenumber8 - 1]) {
    pageVert[pagenumber8 - 1].style.display = 'block';
  }
  if (number1[pagenumber8 - 1]) {
    number1[pagenumber8 - 1].classList.add('pageActive');
  }
}
//=============================price range=======================
const rangeInput = document.querySelectorAll('.multi-range input'),
  priceInput = document.querySelectorAll('.text-violet input'),
  range = document.querySelector('.slider .progress');
let priceGap = 1000;

priceInput.forEach((input) => {
  input.addEventListener('input', (e) => {
    let minPrice = parseInt(priceInput[0].value),
      maxPrice = parseInt(priceInput[1].value);

    if (maxPrice - minPrice >= priceGap && maxPrice <= rangeInput[1].max) {
      if (e.target.className === 'input-min') {
        rangeInput[0].value = minPrice;
        range.style.left = (minPrice / rangeInput[0].max) * 100 + '%';
      } else {
        rangeInput[1].value = maxPrice;
        range.style.right = 100 - (maxPrice / rangeInput[1].max) * 100 + '%';
      }
    }
  });
});

rangeInput.forEach((input) => {
  input.addEventListener('input', (e) => {
    let minVal = parseInt(rangeInput[0].value),
      maxVal = parseInt(rangeInput[1].value);

    if (maxVal - minVal < priceGap) {
      if (e.target.className === 'range-min') {
        rangeInput[0].value = maxVal - priceGap;
      } else {
        rangeInput[1].value = minVal + priceGap;
      }
    } else {
      priceInput[0].value = minVal;
      priceInput[1].value = maxVal;
      range.style.left = (minVal / rangeInput[0].max) * 100 + '%';
      range.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + '%';
    }
  });
});

//======================================= change mode ======================================
function changepage(n) {
  var mode2 = document.getElementsByClassName('hori-list');
  var mode1 = document.getElementsByClassName('vert-list');
  var bordshow1 = document.getElementsByClassName('show-mode-p1');
  var bordshow2 = document.getElementsByClassName('show-mode-p2');

  if (n == 1) {
    mode1[0].style.display = 'block';
    mode2[0].style.display = 'none';
    bordshow2[0].classList.remove('show-mode-border');
    bordshow1[0].classList.add('show-mode-border');
  }
  if (n == 2) {
    mode1[0].style.display = 'none';
    mode2[0].style.display = 'block';
    bordshow1[0].classList.remove('show-mode-border');
    bordshow2[0].classList.add('show-mode-border');
  }
}
//========================================= filter ================================
function filterbox(n) {
  var filterboxEl = document.getElementsByClassName('filter-products-box');
  var blackback = document.getElementsByClassName('background');
  if (n == 1) {
    filterboxEl[0].classList.remove('filter-products-off');
    filterboxEl[0].classList.add('filter-products');
    blackback[0].style.display = 'block';
  }
  if (n == 2) {
    filterboxEl[0].classList.remove('filter-products');
    filterboxEl[0].classList.add('filter-products-off');
    blackback[0].style.display = 'none';
  }
}
//================================= search brand =====================
function searchBrand() {
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById('myInput');
  filter = input.value.toUpperCase();
  ul = document.getElementById('myUL');
  li = ul.getElementsByTagName('li');
  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName('p')[(0, 1)];
    txtValue = a.textContent || a.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = '';
    } else {
      li[i].style.display = 'none';
    }
  }
}
//==================================== filter box ============================
let indexnumber = 0;

function numberplus(n) {
  boxcover((indexnumber += n));
}

function boxcover(n) {
  var detailBox = document.getElementsByClassName('brand-searchbox');
  var img = document.getElementsByClassName('filter-title-img');
  if (n == 1) {
    detailBox[0].classList.remove('brand-off');
    img[1].classList.add('rotate-img');
  }
  if (n == 2) {
    detailBox[0].classList.add('brand-off');
    img[1].classList.remove('rotate-img');
    indexnumber = 0;
  }
}

let indexnumberS = 0;

function clickme(n) {
  boxcover1((indexnumberS += n));
}

function boxcover1(n) {
  var detailBox1 = document.getElementsByClassName('center');
  var img = document.getElementsByClassName('filter-title-img');
  if (n == 1) {
    detailBox1[0].classList.remove('brand-off');
    img[0].classList.add('rotate-img');
  }
  if (n == 2) {
    detailBox1[0].classList.add('brand-off');
    img[0].classList.remove('rotate-img');
    indexnumberS = 0;
  }
}

let indexnumberSS = 0;

function clickmepls(n) {
  boxcover2((indexnumberSS += n));
}

function boxcover2(n) {
  var detailBox2 = document.getElementsByClassName('type-seller');
  var img = document.getElementsByClassName('filter-title-img');
  if (n == 1) {
    detailBox2[0].classList.remove('brand-off');
    img[2].classList.add('rotate-img');
  }
  if (n == 2) {
    detailBox2[0].classList.add('brand-off');
    img[2].classList.remove('rotate-img');
    indexnumberSS = 0;
  }
}
