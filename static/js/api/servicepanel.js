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
const infoFullnameInput = getById('info-fullname-input');
const infoPhoneInput = getById('info-phone-input');
const infoPasswordInput = getById('info-password-input');

(async () => {
  try {
    const response = await axios.get(
      '{% url "ApiServicePanel:servicepanel_user_info" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const userInfo = response.data.result;

    infoFullnameInput.value = userInfo.fullname;
    infoPhoneInput.value = userInfo.phone;

    console.log(response);
  } catch (error) {
    console.log(error);
  }
})();

btnUpdateUser.addEventListener('click', async (event) => {
  event.preventDefault();
  const info = {
    fullname: infoFullnameInput.value,
    phone: infoPhoneInput.value,
    password: infoPasswordInput.value,
  };

  try {
    const response = await axios.put(
      '{% url "ApiServicePanel:servicepanel_edit_account" %}',
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

// services list
const servicesListContent = getById('services-list-content');
const mobileServicesListContent = getById('mobile-services-list-content');
const luncherEditServiceModal = getById('lunch-edit-service-modal');

const inputEditServiceTitle = getById('input-title-edit-service');
const inputEditServiceDescription = getById('input-description-edit-service');
const inputEditServiceCategory = getById('input-category-edit-service');
const inputEditServiceCompany = getById('input-company-edit-service');

const btnEditService = getById('btn-update-service');

const servicesListTemplate = ({ image, title, id, date, number }) => {
  return `
    <div class="mid-table" id="s-l--${id}">
      <div>
          <p>${number}</p>
      </div>
      <div class="mid-table-img">
          <img src="${image}" alt="">
      </div>
      <div>
          <p>${title}</p>
      </div>

      <div>
          <p>${date}</p>
      </div>
      <div>
          <div class="edit-icons">
              <div class="edit-icon" onclick="editService(${id})"></div>
              <div class="trash-icon" onclick="deleteService(${id})"></div>
          </div>
      </div>
    </div>
  `;
};

const mobileServicesListTemplate = ({ image, title, id, date }) => {
  return `
    <div class="all-service-card" id="s-l-m--${id}">
      <div class="fc fc-r1">
          <p class="fc-text1">نام : ${title}</p>
          <img class="fc-img" src="${image}" alt="">
      </div>
      <div class="fc fc-r4">
          <p class="fc-text1">تاریخ</p>
          <p class="fc-text2">${date}</p>
      </div>

      <div class="fc fc-r6">
          <div class="trash-forosh-icon" onclick="deleteService(${id}"></div>
          <div class="edit-forosh-icon" onclick="editService(${id})"></div>
      </div>
    </div>
  `;
};

let services = null;
let idCurrentServiceForEdit = null;
const editService = (id) => {
  const service = services.find((item) => item.id == id);
  idCurrentServiceForEdit = id;

  inputEditServiceTitle.value = service.title;
  inputEditServiceDescription.value = service.description;
  inputEditServiceCategory.value = service.categories.join('/');
  inputEditServiceCompany.value = service.company;

  luncherEditServiceModal.click();
};

const editServiceSubmit = async () => {
  const serviceData = {
    id: idCurrentServiceForEdit,
    title: inputEditServiceTitle.value,
    description: inputEditServiceDescription.value,
    Category: inputEditServiceCategory.value,
    company: inputEditServiceCompany.value,
  };
  try {
    const response = await axios.put(
      '{% url "ApiServicePanel:servicepanel_service_edit" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      },
      serviceData
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
};

const deleteService = async (id) => {
  try {
    const response = await axios.get(
      `{% url "ApiServicePanel:servicepanel_service_delete" %}?id=${id}`,
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    console.log(response);
    if ('message' in response.data) {
      goodFeedback();
      getById(`s-l--${id}`).style.display = 'none';
      getById(`s-l-m--${id}`).style.display = 'none';
    } else {
      badFeedback(response.data);
    }
  } catch (error) {
    console.log(error);
    catchFeedback();
  }
};

(async () => {
  try {
    const response = await axios.get(
      '{% url "ApiServicePanel:servicepanel_service_list" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    services = response.data.results;
    services.forEach((service, key) => {
      servicesListContent.innerHTML += servicesListTemplate({
        ...service,
        number: key + 1,
      });
      mobileServicesListContent.innerHTML +=
        mobileServicesListTemplate(service);
    });
  } catch (error) {
    console.log(error);
  }
})();

// add service
const btnAddService = getById('btn-add-service');
const addServiceImageInput = getById('add-service-image');
const addServiceTitleInput = getById('add-service-title');
const addServiceDescriptionInput = getById('add-service-description');
const addServiceShortDescriptionInput = getById(
  'add-service-short-description'
);
const addServiceCategoryInput = getById('add-service-category');
const addServiceCompanyInput = getById('add-service-company');
const addServiceSubDescriptionInput = getById('add-service-sub-description');

btnAddService.addEventListener('click', async (event) => {
  event.preventDefault();
  const formData = new FormData();
  formData.append('image', addServiceImageInput.files[0]);
  formData.append('title', addServiceTitleInput.value);
  formData.append('description', addServiceDescriptionInput.value);
  formData.append('short_description', addServiceShortDescriptionInput.value);
  formData.append('company', addServiceCompanyInput.value);
  addServiceCategoryInput.value.split('/').forEach((oneCategory) => {
    formData.append('categories', oneCategory);
  });

  try {
    const response = await axios.post(
      '/api/service-panel/servicepanel-service-add/',
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
    console.log(error);
    catchFeedback();
  }
});

//commets
const commentsContent = getById('comments-content');

const commentsTemplate = ({ date, comment, user, service }) => {
  return `
    <div class="comments-box">
      <div class="comment-detail-box">
        <div class="comment-div-img">
        <div class="">
          <p>${date}</p>
        </div>
        </div>
        <div class="top-complaintbox">
            <div>
                <p>${comment}</p>
            </div>
        </div>
        <div>
          <p>آیدی کاربر: ${user}</p>
          <p>آیدی سرویس: ${service}</p>
        </div>
        <div class="div-line2"></div>
      </div>
    </div>
  `;
};

(async () => {
  try {
    const response = await axios.get(
      '{% url "ApiServicePanel:servicepanel_service_comments_list" %}',
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
  } catch (error) {
    console.log(error);
  }
})();

// chart
(async () => {
  try {
    const responseYear = await axios.get(
      '{% url "ApiServicePanel:servicepanel_service_sales_chart_year" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const responseMonth = await axios.get(
      '{% url "ApiServicePanel:servicepanel_service_sales_chart_month" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const responseWeek = await axios.get(
      '{% url "ApiServicePanel:servicepanel_service_sales_chart_week" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const responseDays = await axios.get(
      '{% url "ApiServicePanel:servicepanel_service_sales_chart_day" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const chartDataYear = responseYear.data.total_price;
    const xValuesYear = chartDataYear.map((value, index) => index + 1);
    new Chart('service-chart-year', {
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

    const chartDataMonth = responseMonth.data.total_price;
    const xValuesMonth = chartDataMonth.map((value, index) => index + 1);
    new Chart('service-chart-month', {
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

    const chartDataDay = responseDays.data.total_price;
    const xValuesDay = chartDataDay.map((value, index) => index + 1);
    new Chart('service-chart-day', {
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

    const chartDataWeek = responseWeek.data.total_price;
    const xValuesWeek = chartDataWeek.map((value, index) => index + 1);
    new Chart('service-chart-week', {
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
  } catch (error) {
    console.log(error);
  }
})();

// service orders list content
const serviceOrdersContent = getById('service-orders-list-content');
const desktopnServiceOrdersContent = getById(
  'table-service-orders-list-content'
);

const serviceListOrdersTemplate = ({ user_fullname, date, service }) => {
  return `
    <div class="forosh-card">
      <div class="fc fc-r1">
          <p class="fc-text1">خدمات </p>
          <p class="fc-text2">${service}</p>
      </div>
      <div class="fc fc-r3">
          <p class="fc-text1">${user_fullname}</p>
          <p class="fc-text2">224sdfd4</p>
      </div>
      <div class="fc fc-r4">
          <p class="fc-text1">تاریخ</p>
          <p class="fc-text2">${date}</p>
      </div>
    </div>
  `;
};

const desltopServiceListOrdersTemplate = ({ user_fullname, date, service }) => {
  return `
    <div class="mid-table-cli">

      <div>
          <p>${service}</p>
      </div>
      <div>
          <p>${user_fullname}</p>
      </div>
      <div>
          <p>${date}</p>
      </div>
 
    </div>
  `;
};

(async () => {
  try {
    const response = await axios.get(
      '{% url "ApiServicePanel:servicepanel_service_performed_list" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const serviceOrders = response.data.results;
    serviceOrders.forEach((serviceOrder) => {
      serviceOrdersContent.innerHTML += serviceListOrdersTemplate(serviceOrder);
      desktopnServiceOrdersContent.innerHTML +=
        desltopServiceListOrdersTemplate(serviceOrder);
      serviceOrdersContent.innerHTML += serviceListOrdersTemplate(serviceOrder);
    });
  } catch (error) {
    console.log(error);
  }
})();

// complaints
const complaintsContent = getById('complaints-content');

const complaintsTemplate = ({ text, date, service, phone }) => {
  return `
    <div class="complaint-box">
      <div>
          <p class="">متن شکایت : ${text}</p>
          <p class="">آیدی خدمات : ${service}</p>
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
      '{% url "ApiServicePanel:sellerpanel_products_complaints_list" %}',
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    const complaints = response.data.results;
    complaints.forEach(async (complaint) => {
      const userResponse = await axios.get(
        `{% url "ApiServicePanel:sellerpanel_products_complaints_user_info" %}?id=${complaint.user}`,
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
    });
  } catch (error) {
    console.log(error);
  }
})();
