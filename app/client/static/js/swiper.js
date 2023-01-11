const swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,
  spaceBetween: 20,
  loop: true,
  pagination: {
    el: ".swipPag",
    type: "fraction",
    clickable: true,
  },
  navigation: {
    prevEl: '.slidePrev-btn',
    nextEl: '.slideNext-btn'
  },
});
