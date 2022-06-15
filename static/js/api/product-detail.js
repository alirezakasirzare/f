const token = '{{ token }}';
// general
const getById = (id) => document.getElementById(id);
const id = +window.urlPage.split('/')[3];

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

// add to cart
const btnUpdateUser = getById('add-product-to-card-button');

const colorInput = getById('products-color');
const sizeInput = getById('products-size');
const countInput = getById('counter');

btnUpdateUser.addEventListener('click', async (event) => {
  event.preventDefault();
  console.log({
    color: colorInput.value,
    size: sizeInput.value,
    count: +countInput.innerHTML,
    product: id,
  });
  $.ajax({
    url: '/api/carts/carts-add/',
    type: 'post',
    headers: {
      Authorization: 'Token ' + token,
    },
    data: {
      color: colorInput.value,
      size: sizeInput.value,
      count: +countInput.innerHTML,
      product: id,
    },
    success: (res) => {
      console.log(res);
      if ('message' in res) {
        goodFeedback();
        const cartNumberContent = document.getElementById('cart-number');

        (async () => {
          const response = await axios.get('/api/carts/carts-number/', {
            headers: {
              Authorization: 'Token' + ' ' + tokenMenu,
            },
          });

          const cartNumber = response.data.number;
          cartNumberContent.innerHTML = cartNumber;
        })();
      } else {
        badFeedback(res);
      }
    },
    error: (err) => {},
  });
});

// add comment
const btnAddComment = getById('add-comment-to-product');

const commentText = getById('comment-text-input');

btnAddComment.addEventListener('click', (event) => {
  event.preventDefault();

  $.ajax({
    url: '/api/products/products-comments-add/',
    type: 'post',
    headers: {
      Authorization: 'Token ' + token,
    },
    data: {
      comment: commentText.value,
      product: id,
      user: 1,
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
