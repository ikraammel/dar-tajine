document.addEventListener("DOMContentLoaded", function () {
  const menuToggle = document.getElementById("menu-toggle");
  const submenu = document.querySelector(".submenu");
  const navMenu = document.querySelector(".main-nav ul");
  const hamburger = document.querySelector(".hamburger");

  // Gestion du sous-menu (menu déroulant)
  if (menuToggle && submenu) {
    menuToggle.addEventListener("click", function (event) {
      event.preventDefault();
      submenu.classList.toggle("active");
    });

    // Fermer le sous-menu si clic à l'extérieur
    document.addEventListener("click", function (event) {
      if (
        !menuToggle.contains(event.target) &&
        !submenu.contains(event.target)
      ) {
        submenu.classList.remove("active");
      }
    });
  }

  // Gestion du menu hamburger (pour mobile)
  if (hamburger && navMenu) {
    hamburger.addEventListener("click", function () {
      navMenu.classList.toggle("open");
    });

    // Fermer le menu si clic à l'extérieur
    document.addEventListener("click", function (e) {
      if (
        !hamburger.contains(e.target) &&
        !navMenu.contains(e.target)
      ) {
        navMenu.classList.remove("open");
      }
    });
  }
});
