const token = '2baaeb2c9a639d1dcfc35a70a38ccc12ea004aca';

const contentContainer = document.getElementById('content');

axios
  .get('/api/seller-panel/sellerpanel-users-messages-list/', {
    headers: {
      Authorization: 'Token' + ' ' + token,
    },
  })
  .then((result) => {
    const persons = result.data.results;

    contentContainer.innerHTML = '';
    persons.forEach((person) => {
      contentContainer.innerHTML += `
        <div class="card card-grey">
          <div class="card-chat-list">
            <div class="chat-list-person">
              <img
                src="${
                  person.user_image ||
                  'https://digi1store.com/images/avatar.jpg'
                }"
                alt="avatar"
                class="avatar"
              />
              <div>${person.user_fullname}</div>
            </div>
            <a href="/seller-panel/chat?id=${
              person.user
            }" class="btn btn-outline-primary"
              >دیدن پیام ها</a
            >
          </div>
        </div>
      `;
    });
  })
  .catch((ex) => {
    console.log(ex);
  });
