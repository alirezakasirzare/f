//=========================================== slider product 1 ===========================
var pagenumber1 = 1;
console.log(pagenumber1);
slidechenger1(1);

function plusslides1(n) {
  slidechenger1((pagenumber1 += n));
}

function currentslide1(n) {
  slidechenger1((pagenumber1 = n));
}

function slidechenger1(n) {
  var i;
  var page = document.getElementsByClassName('p1-page');
  var number = document.getElementsByClassName('dot1');
  if (n > page.length) {
    pagenumber1 = 1;
  }
  if (n < 1) {
    pagenumber1 = page.length;
  }
  for (i = 0; i < page.length; i++) {
    page[i].style.display = 'none';
  }
  for (i = 0; i < number.length; i++) {
    number[i].classList.remove('dot-active');
  }
  page[pagenumber1 - 1].style.display = 'block';
  number[pagenumber1 - 1].classList.add('dot-active');
}
//=========================================== slider product 2 ===========================
var pagenumber2 = 1;
slidechenger2(1);

function plusslides2(n) {
  slidechenger2((pagenumber2 += n));
}

function currentslide2(n) {
  slidechenger2((pagenumber2 = n));
}

function slidechenger2(n) {
  var i;
  var page = document.getElementsByClassName('p2-page');
  var number = document.getElementsByClassName('dot2');
  if (n > page.length) {
    pagenumber2 = 1;
  }
  if (n < 1) {
    pagenumber2 = page.length;
  }
  for (i = 0; i < page.length; i++) {
    page[i].style.display = 'none';
  }
  for (i = 0; i < number.length; i++) {
    number[i].classList.remove('dot-active');
  }
  page[pagenumber2 - 1].style.display = 'block';
  number[pagenumber2 - 1].classList.add('dot-active');
}
//=========================================== slider product 3 ===========================
var pagenumber3 = 1;
slidechenger3(1);

function plusslides3(n) {
  slidechenger3((pagenumber3 += n));
}

function currentslide3(n) {
  slidechenger3((pagenumber3 = n));
}

function slidechenger3(n) {
  var i;
  var page = document.getElementsByClassName('p3-page');
  var number = document.getElementsByClassName('dot3');
  if (n > page.length) {
    pagenumber3 = 1;
  }
  if (n < 1) {
    pagenumber3 = page.length;
  }
  for (i = 0; i < page.length; i++) {
    page[i].style.display = 'none';
  }
  for (i = 0; i < number.length; i++) {
    number[i].classList.remove('dot-active');
  }
  page[pagenumber3 - 1].style.display = 'block';
  number[pagenumber3 - 1].classList.add('dot-active');
}
//=========================================== slider product 4 ===========================
var pagenumber4 = 1;
slidechenger4(1);

function plusslides4(n) {
  slidechenger4((pagenumber4 += n));
}

function currentslide4(n) {
  slidechenger4((pagenumber4 = n));
}

function slidechenger4(n) {
  var i;
  var page = document.getElementsByClassName('p4-page');
  var number = document.getElementsByClassName('dot4');
  if (n > page.length) {
    pagenumber4 = 1;
  }
  if (n < 1) {
    pagenumber4 = page.length;
  }
  for (i = 0; i < page.length; i++) {
    page[i].style.display = 'none';
  }
  for (i = 0; i < number.length; i++) {
    number[i].classList.remove('dot-active');
  }
  page[pagenumber4 - 1].style.display = 'block';
  number[pagenumber4 - 1].classList.add('dot-active');
}
