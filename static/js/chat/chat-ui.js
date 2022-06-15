// general
const body = document.body;
// modal
const modalTriggers = [...document.querySelectorAll('[data-modal]')];
modalTriggers.forEach((modalTrigger) => {
  // select modal
  const modalSelector = modalTrigger.dataset.modal;
  const modal = document.querySelector(modalSelector);
  const modalContent = modal.querySelector('.modal');

  // open modal
  modalTrigger.addEventListener('click', (event) => {
    event.preventDefault();
    body.classList.add('overflow-hidden');
    modal.classList.add('show');
  });

  // close modal
  modal.addEventListener('click', () => {
    body.classList.remove('overflow-hidden');
    modal.classList.remove('show');
  });

  modalContent.addEventListener('click', (event) => {
    event.stopPropagation();
  });
});

// close
const closeButtons = [...document.querySelectorAll('[data-close]')];

closeButtons.forEach((closeButton) => {
  // close target event
  closeButton.addEventListener('click', (event) => {
    const modalSelector = closeButton.dataset.close;
    const target = document.querySelector(modalSelector);
    event.preventDefault();
    body.classList.remove('overflow-hidden');
    target.classList.remove('show');
  });
});
