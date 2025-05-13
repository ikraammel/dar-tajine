// Menu déroulant
document.addEventListener("DOMContentLoaded", function () {
  let menuToggle = document.getElementById("menu-toggle");
  let submenu = document.getElementById("submenu");

  if (menuToggle && submenu) {
      menuToggle.addEventListener("click", function (event) {
          event.preventDefault(); // Empêche le lien de recharger la page
          submenu.classList.toggle("active"); // Ajoute ou enlève la classe "active"
      });

      // Fermer le menu si on clique en dehors
      document.addEventListener("click", function (event) {
          if (!menuToggle.contains(event.target) && !submenu.contains(event.target)) {
              submenu.classList.remove("active");
          }
      });
  }
});

