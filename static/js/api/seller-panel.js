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
const updateSellerpanelFullnameInput = getById(
  'update-sellerpanel-fullname-input'
);
const updateSellerpanelPhoneInput = getById('update-sellerpanel-phone-input');
const updateSellerpanelPasswordInput = getById(
  'update-sellerpanel-password-input'
);

(async () => {
  try {
    const response = await axios.get(
      '/api/seller-panel/sellerpanel-user-info/',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const userInfo = response.data.result;

    updateSellerpanelFullnameInput.value = userInfo.fullname;
    updateSellerpanelPhoneInput.value = userInfo.phone;
  } catch (error) {}
})();

btnUpdateUser.addEventListener('click', async (event) => {
  event.preventDefault();
  const info = {
    fullname: updateSellerpanelFullnameInput.value,
    phone: updateSellerpanelPhoneInput.value,
    password: updateSellerpanelPasswordInput.value,
  };

  try {
    const response = await axios.put(
      '{% url "ApiSellerPanel:sellerpanel_edit_account" %}',
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
    catchFeedback();
  }
});

// add products
const btnAddProducts = getById('btn-add-products');
const addProductsImage1Input = getById('add-products-image1-input');
const addProductsImage2Input = getById('add-products-image2-input');
const addProductsImage3Input = getById('add-products-image3-input');
const addProductsImage4Input = getById('add-products-image4-input');
const addProductsImage5Input = getById('add-products-image5-input');
const addProductsTitleInput = getById('add-products-title-input');
const addProductsWeightInput = getById('add-products-weight-input');
const addProductsDimensionsInput = getById('add-products-dimensions-input');
const addProductsSlugInput = getById('add-products-slug-input');
const addProductsDescriptionInput = getById('add-products-description-input');
const addProductsCategoryInput = getById('add-products-category-input');
const addProductsSubCategory1Input = getById(
  'add-products-sub-category1-input'
);
const addProductsSubCategory2Input = getById(
  'add-products-sub-category2-input'
);
const addProductsShortDescriptionInput = getById(
  'add-products-short-description-input'
);
const addProductsPriceInput = getById('add-products-price-input');
const addProductsDiscountedPriceInput = getById(
  'add-products-discounted-price-input'
);
const addProductsColorInput = getById('add-products-color-input');
const addProductsSizeInput = getById('add-products-size-input');
const addProductsInventoryInput = getById('add-products-inventory-input');

btnAddProducts.addEventListener('click', async (event) => {
  event.preventDefault();
  const formData = new FormData();
  formData.append('main_image', addProductsImage1Input.files[0]);
  formData.append('image1', addProductsImage1Input.files[0]);
  formData.append('image2', addProductsImage2Input.files[0]);
  formData.append('image3', addProductsImage3Input.files[0]);
  formData.append('image4', addProductsImage4Input.files[0]);
  formData.append('title', addProductsTitleInput.value);
  formData.append('slug', addProductsSlugInput.value);
  formData.append('weight', addProductsWeightInput.value);
  formData.append('dimensions', addProductsDimensionsInput.value);
  formData.append('description', addProductsDescriptionInput.value);
  formData.append('short_description', addProductsShortDescriptionInput.value);
  formData.append('price', addProductsPriceInput.value);
  addProductsCategoryInput.value.split('/').forEach((oneCategory) => {
    formData.append('maincategories', oneCategory);
  });

  addProductsSubCategory1Input.value.split('/').forEach((oneSubCategory1) => {
    formData.append('subCategories1', oneSubCategory1);
  });

  addProductsSubCategory2Input.value.split('/').forEach((oneSubCategoty2) => {
    formData.append('subCategories2', oneSubCategoty2);
  });

  addProductsColorInput.value.split('/').forEach((oneColor) => {
    formData.append('colors', oneColor);
  });

  addProductsSizeInput.value.split('/').forEach((oneSize) => {
    formData.append('sizes', oneSize);
  });

  formData.append('inventory', addProductsInventoryInput.value);

  try {
    const response = await axios.post(
      '/api/seller-panel/sellerpanel-products-add/',
      formData,
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
    catchFeedback();
  }
});

// products list
const peoductsListContent = getById('products-list-content');
const luncherEditProductModal = getById('lunch-edit-product-modal');

const inputEditProductTitle = getById('input-title-edit-product');
const inputEditProductDimensions = getById('input-dimensions-edit-product');
const inputEditProductWeight = getById('input-weight-edit-product');
const inputEditProductSlug = getById('input-slug-edit-product');
const inputEditProductDescription = getById('input-description-edit-product');
const inputEditProductShortDescription = getById(
  'input-short-description-edit-product'
);
const inputEditProductPrice = getById('input-price-edit-product');
const inputEditProductDiscontedPrice = getById(
  'input-disconted-price-edit-product'
);
const inputEditProductCategory = getById('input-category-edit-product');
const inputEditProductCategory1 = getById('input-sub-category1-edit-product');
const inputEditProductCategory2 = getById('input-sub-category2-edit-product');
const inputEditProductColor = getById('input-color-edit-product');
const inputEditProductSize = getById('input-size-edit-product');
const inputEditProductInventory = getById('input-inventory-edit-product');

const btnEditProduct = getById('btn-update-product');

const profuctsListTemplate = ({ main_image, id, date }) => {
  return `
    <div class="all-forosh-tablet" id="p-l--${id}">
      <div class="all-service-card">
          <div class="fc fc-r1">
              <p class="fc-text1">نام </p>
              <img class="fc-img" src="${main_image}" alt="">
          </div>
          <div class="fc fc-r2">
              <p class="fc-text1">کد خدمت </p>
              <p class="fc-text2">${id}</p>
          </div>

          <div class="fc fc-r4">
              <p class="fc-text1">تاریخ</p>
              <p class="fc-text2">${date}</p>
          </div>

          <div class="fc fc-r6">
              <div class="trash-forosh-icon" onclick="deleteProduct(${id})"></div>
              <div class="edit-forosh-icon" onclick="editProduct(${id})"></div>
          </div>
      </div>
    </div>
  `;
};

const deleteProduct = async (id) => {
  try {
    const response = await axios.get(
      `{% url "ApiSellerPanel:sellerpanel_products_delete" %}?id=${id}`,
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    console.log(response);
    if ('message' in response.data) {
      goodFeedback();
      getById(`p-l--${id}`).style.display = 'none';
    } else {
      badFeedback(response.data);
    }
  } catch (error) {
    catchFeedback();
  }
};

let products = null;
let idCurrentProductForEdit = null;
const editProduct = (id) => {
  const product = products.find((item) => item.id == id);
  idCurrentProductForEdit = id;

  inputEditProductTitle.value = product.title;
  inputEditProductDimensions.value = product.dimensions;
  inputEditProductWeight.value = 'product.';
  inputEditProductSlug.value = product.slug;
  inputEditProductDescription.value = product.description;
  inputEditProductShortDescription.value = product.short_description;
  inputEditProductPrice.value = product.price;
  inputEditProductDiscontedPrice.value = product.discounted_price;
  inputEditProductCategory.value = product.maincategories.join('/');
  inputEditProductCategory1.value = product.subCategories1.join('/');
  inputEditProductCategory2.value = product.subCategories2.join('/');
  inputEditProductColor.value = product.colors.join('/');
  inputEditProductSize.value = product.sizes.join('/');
  inputEditProductInventory.value = product.inventory;

  luncherEditProductModal.click();
};

const editProductSubmit = async () => {
  const info = {
    id: idCurrentProductForEdit,
    title: inputEditProductTitle.value,
    dimensions: inputEditProductDimensions.value,
    weight: inputEditProductWeight.value,
    slug: inputEditProductSlug.value,
    description: inputEditProductDescription.value,
    short_description: inputEditProductShortDescription.value,
    price: inputEditProductPrice.value,
    discounted_price: inputEditProductDiscontedPrice.value,
    maincategories: inputEditProductCategory.value,
    subCategories1: inputEditProductCategory1.value,
    subCategories2: inputEditProductCategory2.value,
    colors: inputEditProductColor.value,
    sizes: inputEditProductSize.value,
    inventory: inputEditProductInventory.value,
  };

  try {
    const response = await axios.post(
      '{% url "ApiSellerPanel:sellerpanel_products_edit" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      },
      info
    );

    console.log(response);
    if ('message' in response.data) {
      goodFeedback();
    } else {
      badFeedback(response.data);
    }
  } catch (error) {
    catchFeedback();
  }
};

(async () => {
  try {
    const response = await axios.get(
      '{% url "ApiSellerPanel:sellerpanel_products_list" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    products = response.data.results;
    products.forEach((product) => {
      peoductsListContent.innerHTML += profuctsListTemplate(product);
    });
  } catch (error) {}
})();

// commets
const commentsContent = getById('comments-content');

const commentsTemplate = ({ date, comment }) => {
  return `
    <div class="comments-box">
      <div class="comment-detail-boxd">
          <div class="top-complaintbox2">

            <div>
            <p>${comment}</p>
            <p>${date}</p>
            </div>
          </div>

          <div class="div-line2"></div>
      </div>

    </div>
  `;
};

(async () => {
  try {
    const response = await axios.get(
      '{% url "ApiSellerPanel:sellerpanel_products_comments_list" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const comments = response.data.results;
    comments.forEach((comment) => {
      commentsContent.innerHTML += commentsTemplate(comment);
    });
  } catch (error) {}
})();

// chart
(async () => {
  try {
    const responseYear = await axios.get(
      '{% url "ApiSellerPanel:sellerpanel_products_sales_chart_year" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const chartDataYear = responseYear.data.total_price;
    const xValuesYear = chartDataYear.map((value, index) => index + 1);
    new Chart('sell-chart-year', {
      type: 'line',
      data: {
        labels: xValuesYear,
        datasets: [
          {
            lineTension: 0,
            data: chartDataYear,
            borderColor: '#EC6666',
            fill: false,
          },
        ],
      },
      options: {
        legend: { display: false },
      },
    });

    const responseMonth = await axios.get(
      '{% url "ApiSellerPanel:sellerpanel_products_sales_chart_month" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const chartDataMonth = responseMonth.data.total_price;
    const xValuesMonth = chartDataMonth.map((value, index) => index + 1);
    new Chart('sell-chart-month', {
      type: 'line',
      data: {
        labels: xValuesMonth,
        datasets: [
          {
            lineTension: 0,
            data: chartDataMonth,
            borderColor: '#EC6666',
            fill: false,
          },
        ],
      },
      options: {
        legend: { display: false },
      },
    });

    const responseWeek = await axios.get(
      '{% url "ApiSellerPanel:sellerpanel_products_sales_chart_week" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const chartDataWeek = responseWeek.data.total_price;
    const xValuesWeek = chartDataWeek.map((value, index) => index + 1);
    new Chart('sell-chart-week', {
      type: 'line',
      data: {
        labels: xValuesWeek,
        datasets: [
          {
            lineTension: 0,
            data: chartDataWeek,
            borderColor: '#EC6666',
            fill: false,
          },
        ],
      },
      options: {
        legend: { display: false },
      },
    });

    const responseDays = await axios.get(
      '{% url "ApiSellerPanel:sellerpanel_products_sales_chart_day" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const chartDataDay = responseDays.data.total_price;
    const xValuesDay = chartDataDay.map((value, index) => index + 1);
    new Chart('sell-chart-day', {
      type: 'line',
      data: {
        labels: xValuesDay,
        datasets: [
          {
            lineTension: 0,
            data: chartDataDay,
            borderColor: '#EC6666',
            fill: false,
          },
        ],
      },
      options: {
        legend: { display: false },
      },
    });
  } catch (error) {}
})();

// complaints
const complaintsContent = getById('complaints-content');

const complaintsTemplate = ({ text, date, product, phone }) => {
  return `
    <div class="complaint-box">
      <div>
          <p class="">متن شکایت : ${text}</p>
          <p class="">آیدی محصول : ${product}</p>
          <p class="">شماره موبایل کاربر : ${phone}</p>
          <p class="">${date}</p>
      </div>
      <div class="div-line"></div>
    </div>
  `;
};

(async () => {
  try {
    const response = await axios.get(
      '{% url "ApiSellerPanel:sellerpanel_products_complaints_list" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const complaints = response.data.results;
    complaints.forEach(async (complaint) => {
      try {
        const userResponse = await axios.get(
          `{% url "ApiSellerPanel:sellerpanel_products_complaints_user_info" %}?id=${complaint.user}`,
          {
            headers: {
              Authorization: 'Token' + ' ' + token,
            },
          }
        );

        const user = userResponse.data;

        complaintsContent.innerHTML += complaintsTemplate({
          ...complaint,
          ...user,
        });
      } catch (error) {}
    });
  } catch (error) {}
})();

// add shop
const btnAddShop = getById('btn-add-shop');
const addShopImageInput = getById('add-shop-image');
const addShopTitleInput = getById('add-shop-title');
const addShopDescriptionInput = getById('add-shop-description');
const addShoplicenceInput = getById('add-shop-licence');
const addShopeCategoryInput = getById('add-shop-category');

btnAddShop.addEventListener('click', async (event) => {
  event.preventDefault();

  const formData = new FormData();
  formData.append('business_image', addShopImageInput.files[0]);
  formData.append('business_name', addShopTitleInput.value);
  formData.append('business_description', addShopDescriptionInput.value);
  formData.append('business_license', addShoplicenceInput.files[0]);
  addShopeCategoryInput.value.split('/').forEach((oneCategory) => {
    formData.append('business_categories', oneCategory);
  });

  try {
    const response = await axios.post(
      '{% url "ApiSellerPanel:sellerpanel_shop_add" %}',
      formData,
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
    catchFeedback();
  }
});
