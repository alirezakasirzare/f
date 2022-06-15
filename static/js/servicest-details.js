//================================= chat box ====================================
$(function () {
  var INDEX = 0;
  $('#chat-submit').click(function (e) {
    e.preventDefault();
    var msg = $('#chat-input').val();
    if (msg.trim() == '') {
      return false;
    }
    generate_message(msg, 'self');
    var buttons = [
      {
        name: 'Existing User',
        value: 'existing',
      },
      {
        name: 'New User',
        value: 'new',
      },
    ];
    setTimeout(function () {
      generate_message(msg, 'user');
    }, 1000);
  });

  function generate_message(msg, type) {
    INDEX++;
    var str = '';
    str += "<div id='cm-msg-" + INDEX + '\' class="chat-msg ' + type + '">';
    str += '          <span class="msg-avatar">';
    str +=
      '            <img src="https://image.crisp.im/avatar/operator/196af8cc-f6ad-4ef7-afd1-c45d5231387c/240/?1483361727745">';
    str += '          </span>';
    str += '          <div class="cm-msg-text">';
    str += msg;
    str += '          </div>';
    str += '        </div>';
    $('.chat-logs').append(str);
    $('#cm-msg-' + INDEX)
      .hide()
      .fadeIn(300);
    if (type == 'self') {
      $('#chat-input').val('');
    }
    $('.chat-logs')
      .stop()
      .animate({ scrollTop: $('.chat-logs')[0].scrollHeight }, 1000);
  }

  function generate_button_message(msg, buttons) {
    /* Buttons should be object array 
              [
                {
                  name: 'Existing User',
                  value: 'existing'
                },
                {
                  name: 'New User',
                  value: 'new'
                }
              ]
            */
    INDEX++;
    var btn_obj = buttons
      .map(function (button) {
        return (
          '              <li class="button"><a href="javascript:;" class="btn btn-primary chat-btn" chat-value="' +
          button.value +
          '">' +
          button.name +
          '</a></li>'
        );
      })
      .join('');
    var str = '';
    str += "<div id='cm-msg-" + INDEX + '\' class="chat-msg user">';
    str += '          <span class="msg-avatar">';
    str +=
      '            <img src="https://image.crisp.im/avatar/operator/196af8cc-f6ad-4ef7-afd1-c45d5231387c/240/?1483361727745">';
    str += '          </span>';
    str += '          <div class="cm-msg-text">';
    str += msg;
    str += '          </div>';
    str += '          <div class="cm-msg-button">';
    str += '            <ul>';
    str += btn_obj;
    str += '            </ul>';
    str += '          </div>';
    str += '        </div>';
    $('.chat-logs').append(str);
    $('#cm-msg-' + INDEX)
      .hide()
      .fadeIn(300);
    $('.chat-logs')
      .stop()
      .animate({ scrollTop: $('.chat-logs')[0].scrollHeight }, 1000);
    $('#chat-input').attr('disabled', true);
  }

  $(document).delegate('.chat-btn', 'click', function () {
    var value = $(this).attr('chat-value');
    var name = $(this).html();
    $('#chat-input').attr('disabled', false);
    generate_message(name, 'self');
  });

  $('#chat-circle').click(function () {
    $('#chat-circle').toggle('scale');
    $('.chat-box').toggle('scale');
  });

  $('.chat-box-toggle').click(function () {
    $('#chat-circle').toggle('scale');
    $('.chat-box').toggle('scale');
  });
});
// ==========================DETAILS_TAB==================

var detailstabLinks = document.querySelectorAll('.detailstablinks');
var detailstabContent = document.querySelectorAll('.detailstabcontent');

detailstabLinks.forEach(function (el) {
  el.addEventListener('click', detailsopenTabs);
});

function detailsopenTabs(el) {
  var detailsbtnTarget = el.currentTarget;
  var detailsvaluetxt = detailsbtnTarget.dataset.valuetxt;

  detailstabContent.forEach(function (el) {
    el.classList.remove('detailsactive');
  });

  detailstabLinks.forEach(function (el) {
    el.classList.remove('detailsactive');
  });

  document.querySelector('#' + detailsvaluetxt).classList.add('detailsactive');

  detailsbtnTarget.classList.add('detailsactive');
}

// ==========================DETAILS_TAB==================
var pagenumber1 = 1;
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

  if (pagenumber1 - 1) {
    page[pagenumber1 - 1].style.display = 'block';
    number[pagenumber1 - 1].classList.add('dot-active');
  }
}
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

// slider
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
