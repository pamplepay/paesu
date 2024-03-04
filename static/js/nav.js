const toggleBtn = document.querySelector(".navbar__toogleBtn");
const menu = document.querySelector(".navbar__menu");
const toggleSelect = document.querySelector(".select__button");
const selectContent = document.querySelector(".select__content");

toggleBtn.addEventListener("click", () => {
  menu.classList.toggle("active");
});
