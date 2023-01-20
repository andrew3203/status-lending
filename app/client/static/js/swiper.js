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
    319: {
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

const swiper3 = new Swiper(".mySwiper3", {
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
    319: {
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

const swiper4 = new Swiper(".mySwiper4", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  preloadImages: false,
  lazy: true,
  centeredSlides: true,
  effect: "fade",
  navigation: {
    prevEl: '.slidePrev-btn23',
    nextEl: '.slideNext-btn23'
  },
});
