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

const swiper2 = new Swiper(".mySwiper2", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  centeredSlides: true,
  effect: "fade",
  navigation: {
    prevEl: '.slidePrev-btn2',
    nextEl: '.slideNext-btn2'
  },
});
