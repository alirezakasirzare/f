const token = '5927a52b6ec44eb2e0735f70248a4b8a42d0ce6e';
const SITE_BASE_URL = 'http://alireza.ir/';
// general
const $ = (id) => document.getElementById(id);

// varibles
const chatForm = $('send-message');
const chatTextInput = $('chat-input-send');
const chatFileInput = $('chat-input-file');

const chatBtnSend = $('chat-btn-send');
const chatBtnFile = $('chat-btn-file');

const payForm = $('pay-form');
const pricePayInput = $('input-pay');
const resultPayLinkInput = $('input-pay-link');

const payBtnSubmit = $('pay-btn-submit');
const payLinkModalOpener = $('open-result-pay-link');

const params = new Proxy(new URLSearchParams(window.location.search), {
  get: (searchParams, prop) => searchParams.get(prop),
});

// dom
const contentContainer = $('content');

const textMessage = (is_service, text) => {
  return `
    <div class="card card-${is_service ? 'primary' : 'secondary'} card-${
    is_service ? 'my' : 'friend'
  }-message">
      <p>${text}</p>
    </div>
  `;
};

const fileMessage = (is_service, file) => {
  return `
  <div class="card card-${is_service ? 'primary' : 'secondary'} card-${
    is_service ? 'my' : 'friend'
  }-message">
    <a href="${file}" class="file-card-link">
      <div class="file-icon-wrapper">
        <i class="far fa-file-alt"></i>
      </div>
      <p>فایل</p>
    </a>
  </div>
  `;
};

const addMessageToDom = (message) => {
  if (message.text) {
    contentContainer.innerHTML += textMessage(message.is_service, message.text);
  } else if (message.file) {
    contentContainer.innerHTML += fileMessage(message.is_service, message.file);
  }

  window.scrollTo({
    left: 0,
    top: document.body.scrollHeight,
    behavior: 'smooth',
  });
};

// control pay form
payForm.addEventListener('submit', (e) => {
  e.preventDefault();
});

payBtnSubmit.addEventListener('click', async () => {
  const price = +pricePayInput.value;

  if (!price) {
    return;
  }

  const response = await axios.post(
    '/api/service-panel/servicepanel-create-link-payment/',
    {
      user: +params.id,
      service: +params.service,
      price: price,
    },
    {
      headers: {
        Authorization: 'Token' + ' ' + token,
        'Content-Type': 'application/json',
      },
    }
  );

  resultPayLinkInput.value = SITE_BASE_URL + response.data.link;
  payLinkModalOpener.click();
});

// control inputes chat form
chatForm.addEventListener('submit', (e) => {
  e.preventDefault();
});

chatTextInput.addEventListener('input', () => {
  if (chatTextInput.value.length) {
    chatBtnSend.classList.remove('hidden');
    chatBtnFile.classList.add('hidden');
  } else {
    chatBtnFile.classList.remove('hidden');
    chatBtnSend.classList.add('hidden');
  }
});

chatFileInput.addEventListener('change', async () => {
  try {
    const formData = new FormData();
    formData.append('user', +params.id);
    formData.append('service', +params.service);
    formData.append('file', chatFileInput.files[0]);
    const response = await axios.post(
      '/api/service-panel/servicepanel-messages-add/',
      formData,
      {
        headers: {
          'Content-Type': 'multipart/form-data',
          Authorization: 'Token' + ' ' + token,
        },
      }
    );

    if (response && response.data.message == 'با موفقیت ثبت شد') {
      window.location.reload();
    }
  } catch (ex) {
    console.log(ex);
  }
});

chatBtnFile.addEventListener('click', () => {
  chatFileInput.click();
});

chatBtnSend.addEventListener('click', async () => {
  try {
    // do : open loading modal
    const response = await axios.post(
      '/api/service-panel/servicepanel-messages-add/',
      {
        user: +params.id,
        service: +params.service,
        text: chatTextInput.value,
      },
      {
        headers: {
          Authorization: 'Token' + ' ' + token,
          'Content-Type': 'application/json',
        },
      }
    );
    if (response && response.data.message == 'با موفقیت ثبت شد') {
      const myNewMessage = {
        text: chatTextInput.value,
        file: null,
        is_service: true,
      };
      addMessageToDom(myNewMessage);
      chatTextInput.value = '';
    } else {
      // alert('bad');
    }
  } catch (error) {
    console.log(error);
  }
});

// load data

axios
  .get(
    `/api/service-panel/servicepanel-messages-list-filter/?id=${params.id}&service=${params.service}`,
    {
      headers: {
        Authorization: 'Token' + ' ' + token,
      },
    }
  )
  .then((result) => {
    const messages = [...result.data.results].reverse();
    messages.forEach((message) => {
      addMessageToDom(message);
    });
  })
  .catch((ex) => {
    console.log(ex);
  });
