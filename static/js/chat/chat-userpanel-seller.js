const token = '3ee39dbce469ce448d2004987ae09f5ddb6df759';

// general
const $ = (id) => document.getElementById(id);

// varibles
const chatForm = $('send-message');
const chatTextInput = $('chat-input-send');
const chatFileInput = $('chat-input-file');

const chatBtnSend = $('chat-btn-send');
const chatBtnFile = $('chat-btn-file');

const params = new Proxy(new URLSearchParams(window.location.search), {
  get: (searchParams, prop) => searchParams.get(prop),
});

// dom
const contentContainer = $('content');

const textMessage = (is_seller, text) => {
  return `
    <div class="card card-${is_seller ? 'primary' : 'secondary'} card-${
    is_seller ? 'my' : 'friend'
  }-message">
      <p>${text}</p>
    </div>
  `;
};

const fileMessage = (is_seller, file) => {
  return `
  <div class="card card-${is_seller ? 'primary' : 'secondary'} card-${
    is_seller ? 'my' : 'friend'
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
    contentContainer.innerHTML += textMessage(!message.is_seller, message.text);
  } else if (message.file) {
    contentContainer.innerHTML += fileMessage(!message.is_seller, message.file);
  }

  window.scrollTo({
    left: 0,
    top: document.body.scrollHeight,
    behavior: 'smooth',
  });
};

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
    formData.append('seller', +params.seller);
    formData.append('file', chatFileInput.files[0]);
    const response = await axios.post(
      '/api/user-panel/userpanel-seller-messages-add/',
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
    } else {
      // alert('bad');
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
      '/api/user-panel/userpanel-seller-messages-add/',
      {
        seller: +params.seller,
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
        is_seller: false,
      };
      addMessageToDom(myNewMessage);
      chatTextInput.value = '';
    }
  } catch (error) {
    console.log(error);
  }
});

// load data

axios
  .get(
    `/api/user-panel/userpanel-seller-messages-list-filter/?id=${params.seller}`,
    {
      headers: {
        Authorization: 'Token' + ' ' + token,
      },
    }
  )
  .then((result) => {
    const messages = [...result.data.results].reverse();

    contentContainer.innerHTML = '';
    messages.forEach((message) => {
      const messages = [...result.data.results].reverse();
      messages.forEach((message) => {
        addMessageToDom(message);
      });
    });
  })
  .catch((ex) => {
    console.log(ex);
  });
