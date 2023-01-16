const swiper = new Swiper(".mySwiper", {
  slidesPerView: 3,
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
  breakpoints: {
    // when window width is >= 320px
    320: {
        slidesPerView: 1,
        spaceBetween: 10,
        slideToClickedSlide: true,
    },
    // when window width is >= 768px
    768: {
        slidesPerView: 3,
        spaceBetween: 20,
        slideToClickedSlide: true,
    },
}
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
