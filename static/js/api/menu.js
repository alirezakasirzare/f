const tokenMenu = '4035f41454223aa5595a76d9accea48d54604214';

// general
const getById2 = (id) => document.getElementById(id);

// cart number
const cartNumberContent = getById2('cart-number');

(async () => {
  try {
    const response = await axios.get('/api/carts/carts-number/', {
      headers: {
        Authorization: 'Token' + ' ' + tokenMenu,
      },
    });

    const cartNumber = response.data.number;

    cartNumberContent.innerHTML = cartNumber;
  } catch (ex) {
    cartNumberContent.innerHTML = 0;
  }
})();
