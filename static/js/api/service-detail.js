const token = '{{ token }}';
// general
const getById = (id) => document.getElementById(id);
var urlPage2 = window.location.pathname;
var substrings2 = urlPage2.split('/');
var id = substrings2[3];

// feedback
const feedbackLuncher = $('#lunch-feedback');
const feedbackContent = $('#feedback');

const catchFeedback = () => {
  feedbackContent.css('direction', 'rtl');

  feedbackContent.text('خطا');
  feedbackLuncher.click();
};

const goodFeedback = () => {
  feedbackContent.css('direction', 'rtl');
  feedbackContent.text('موفقیت');
  feedbackLuncher.click();
};

const badFeedback = (data) => {
  let content = '';
  feedbackContent.css('direction', 'ltr');

  $.map(data, function (value, key) {
    content += key + ' : ' + value;
  });
  feedbackContent.text(content);
  feedbackLuncher.click();
};

// add comment
const btnAddComment = getById('add-comment-to-service');

const commentText = getById('comment-text-input');

btnAddComment.addEventListener('click', (event) => {
  event.preventDefault();

  $.ajax({
    url: '/api/services/services-comments-add/',
    type: 'post',
    headers: {
      Authorization: 'Token ' + token,
    },
    data: {
      comment: commentText.value,
      service: id,
    },
    success: (res) => {
      console.log(res);
      if ('message' in res) {
        goodFeedback();
      } else {
        badFeedback(res);
      }
    },
    error: (err) => {
      catchFeedback();
    },
  });
});
