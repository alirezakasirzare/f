const token = '{{ token }}';

// general
const getById = (id) => document.getElementById(id);

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

// update info
const btnUpdateUser = getById('btn-update-user-info');
const updateUserinfoFullnameInput = getById('update-userinfo-fullname-input');
const updateUserinfoPhoneInput = getById('update-userinfo-phone-input');
const updateUserinfoPasswordInput = getById('update-userinfo-password-input');

(async () => {
  try {
    const response = await axios.get('{% url "ApiUserPanel:userpanel_user_info" %}', {
      headers: {
        Authorization: 'Token' + ' ' + token,
      },
    });

    const userInfo = response.data.result;

    updateUserinfoFullnameInput.value = userInfo.fullname;
    updateUserinfoPhoneInput.value = userInfo.phone;
  } catch (error) {}
})();

btnUpdateUser.addEventListener('click', async (event) => {
  event.preventDefault();
  const info = {
    fullname: updateUserinfoFullnameInput.value,
    phone: updateUserinfoPhoneInput.value,
    password: updateUserinfoPasswordInput.value,
  };

  try {
    const response = await axios.put(
      '{% url "ApiUserPanel:userpanel_edit_account" %}',
      info,
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    console.log(response);
    if ('message' in response.data) {
      goodFeedback();
    } else {
      badFeedback(response.data);
    }
  } catch (error) {
    console.log(error);
    catchFeedback();
  }
});

// comments
const commentsContent = getById('comments-content');

const commentTemplate = ({ product_image, product_title, comment, jdate }) => {
  return `
    <div class="user-history-mainbox">
      <div class="user-history-box">
        <div class="user-history-box-right">
          <img
            src="${product_image}"
            alt="${product_title} "
            class="user-comments-img"
          />
          <div class="user-comments-text">
            <h2>${product_title}</h2>
            <p>${comment}</p>
          </div>
        </div>
        <div class="user-history-box-left">
          <div>
            <p>${jdate}</p>
          </div>
        </div>
      </div>
      <div class="div-line"></div>
    </div>
  `;
};

(async () => {
  try {
    const response = await axios.get(
      '{% url "ApiUserPanel:userpanel_products_comments_list" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const comments = response.data.results;
    comments.forEach((comment) => {
      commentsContent.innerHTML += commentTemplate(comment);
    });
  } catch (error) {}
})();

// discounts
const discountsContent = getById('discounts-content');

const discountsTemplate = ({
  title,
  price,
  main_image,
  discounted_price,
  id,
  slug,
}) => {
  return `
    <div class="user-history-mainbox">
      <div class="user-history-box">
        <div class="user-history-box-right">
          <img class="user-discount-img" src="${main_image}" />
          <div class="user-discount-text">
            <h3>${title}</h3>
            <p>قیمت اولیه : ${price}</p>
          </div>
        </div>
        <div class="user-history-box-left">
          <a href="/products/detail/${id}/${slug}/">
            <div class="user-history-lefticon"></div>
          </a>
          <div class="user-discount-btn">
            <p>${discounted_price}</p>
          </div>
        </div>
      </div>
      <div class="div-line"></div>
    </div>
  `;
};

(async () => {
  try {
    const response = await axios.get('/api/products/products-discounts/', {
      headers: {
        Authorization: 'Token' + ' ' + token,
      },
    });

    const discounts = response.data.results;
    discounts.forEach((discount) => {
      discountsContent.innerHTML += discountsTemplate(discount);
    });
  } catch (error) {}
})();

// scores
const scoresContent = getById('scores-content');
const scoreTemplate = ({ score }) => {
  return `
    <div class="user-history-mainbox">
      <div class="user-history-box">
        <div class="user-history-box-right">
          <img
            src="/media/productsImage/1_cwSnUZ5.jpg"
            class="user-discount-img"
          />
          <div class="user-score-text">
            <h2>چاپ فوری</h2>
          </div>
        </div>
        <div class="user-history-box-left">
          <div class="rate">
          ${'<i class="fa fa-star"></i>'.repeat(score)}
          </div>
        </div>
      </div>
      <div class="div-line"></div>
    </div>
  `;
};

(async () => {
  try {
    const response = await axios.get(
      '{% url "ApiUserPanel:userpanel_products_scores_list" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const scores = response.data.results;
    scores.forEach((score) => {
      scoresContent.innerHTML += scoreTemplate(score);
    });
  } catch (error) {}
})();

// history products
const historyProductsContent = getById('history-products-content');
const historyProductsTemplate = ({ price, description }) => {
  return `
    <div class="user-history-mainbox">
      <div class="user-history-box">
        <div class="user-history-box-right">
        <!--
          <img
            src="{% static 'img/pic-29.png' %}"
            class="user-history-img"
          />
          <img
            src="{% static 'img/pic-32.png' %}"
            class="user-history-img"
          />
          <img
            src="{% static 'img/pic-13.png' %}"
            class="user-history-img"
          />
          -->
          <h3 class="user-history-text">${description}</h3>
        </div>
        <div class="user-history-box-left">
          <div class="user-history-lefticon"></div>
          <h3 class="user-history-text">${price}</h3>
        </div>
      </div>
      <div class="div-line"></div>
    </div>
  `;
};

(async () => {
  try {
    const response = await axios.get(
      '{% url "ApiUserPanel:userpanel_order_history" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const productHistorys = response.data.results;
    productHistorys.forEach((productHistory) => {
      historyProductsContent.innerHTML +=
        historyProductsTemplate(productHistory);
    });
  } catch (error) {}
})();

// recived services
const recivedServicesContent = getById('recived-services-content');
const recivedServicesTemplate = ({ jdate, price }) => {
  return `
    <div class="user-history-mainbox">
      <div class="user-history-box">
        <div class="user-history-box-right">
          <h3 class="user-history-text">
          ${jdate}
          </h3>
        </div>
        <div class="user-history-box-left">
          <h3 class="user-history-text">${price}</h3>
        </div>
      </div>
      <div class="div-line"></div>
    </div>
  `;
};

(async () => {
  try {
    const response = await axios.get(
      '{% url "ApiUserPanel:userpanel_services_received" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const recivedServices = response.data.results;
    recivedServices.forEach((recivedService) => {
      recivedServicesContent.innerHTML +=
        recivedServicesTemplate(recivedService);
    });
  } catch (error) {}
})();
