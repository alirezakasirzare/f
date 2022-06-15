const token = '3ee39dbce469ce448d2004987ae09f5ddb6df759';

const contentContainer = document.getElementById('content');

const sellerPersons = axios.get(
  '/api/user-panel/userpanel-seller-users-messages-list/',
  {
    headers: {
      Authorization: 'Token' + ' ' + token,
    },
  }
);
const servicePersons = axios.get(
  '/api/user-panel/userpanel-service-users-messages-list/',
  {
    headers: {
      Authorization: 'Token' + ' ' + token,
    },
  }
);

const renderCards = (image, name, link) => {
  return `
  <div class="card card-grey">
    <div class="card-chat-list">
      <div class="chat-list-person">
        <img
          src="${image || 'https://digi1store.com/images/avatar.jpg'}"
          alt="avatar"
          class="avatar"
        />
        <div>${name}</div>
      </div>
      <a href="${link}" class="btn btn-outline-primary"
        >دیدن پیام ها</a
      >
    </div>
  </div>
 `;
};

axios
  .all([sellerPersons, servicePersons])
  .then((result) => {
    const resultSallerpersons = result[0].data.results;
    const resultServicepersons = result[1].data.results;

    contentContainer.innerHTML = '';
    resultSallerpersons.forEach((person) => {
      const link = `/user-panel/chat-seller?id=${person.user}&seller=${person.seller}`;
      contentContainer.innerHTML += renderCards(
        person.seller_image,
        person.seller_fullname,
        link
      );
    });

    resultServicepersons.forEach((person) => {
      const link = `/user-panel/chat-service?id=${person.user}&service=${person.service}`;
      contentContainer.innerHTML += renderCards(
        person.service_image,
        person.service_fullname,
        link
      );
    });
  })
  .catch((ex) => {
    console.log(ex);
  });
