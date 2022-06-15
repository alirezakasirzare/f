const token = '5927a52b6ec44eb2e0735f70248a4b8a42d0ce6e';

const contentContainer = document.getElementById('content');

axios
  .get('/api/service-panel/servicepanel-users-messages-list/', {
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
            <a href="/service-panel/chat?${
              'id=' + person.user + '&' + 'service=' + person.service
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
