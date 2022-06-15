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
// cart factor list
const cartFactorContent = getById('factor-content');
const factorPriceContent = getById('factor-price');

const cartFactorTemplate = ({ title, price, color, size, product, id }) => {
  return `
    <div class="factor-product" id="o-l--${id}">

      <div class="factor-product-detail">
        <a href="#">${title}</a>
        <div class="color-size">
        <div class="size">
          <p>${color}</p>
        </div>
          <div class="size">
            <p>${size}</p>
          </div>
          <button class="btn btn-secondary" onclick="deleteProductFrom(${product},${id},${price})">
            <i class="fa fa-trash"></i>
          </button>
        </div>
      </div>
      <div class="price-number">
        <p class="price-product">${price}</p>
        <div></div>
      </div>
    </div>
  `;
};

const deleteProductFrom = async (product, id, price) => {
  try {
    const response = await axios.get(
      `{% url "ApiCarts:carts_remove"  %}?productid=${product}&orderid=${id}`,
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    console.log(response);
    if ('message' in response.data) {
      goodFeedback();
      getById(`o-l--${id}`).style.display = 'none';
      factorPriceContent.innerHTML = +factorPriceContent.innerHTML - price;
    } else {
      badFeedback(response.data);
    }

    // window.location.reload();
  } catch (ex) {
    console.log(ex);
  }
};

(async () => {
  const response = await axios.get('{% url "ApiCarts:carts_list" %}', {
    headers: {
      Authorization: 'Token' + ' ' + token,
    },
  });

  let factorPrice = 0;
  const cardProducts = response.data.results;
  cardProducts.forEach((product) => {
    console.log(product);
    factorPrice += product.price;
    cartFactorContent.innerHTML += cartFactorTemplate(product);
  });

  factorPriceContent.innerHTML = factorPrice;
})();
