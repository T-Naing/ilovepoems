document.addEventListener("DOMContentLoaded", function () {
  const menuToggle = document.getElementById("menu-toggle");
  const navContainer = document.querySelector(".nav-links-container");
  const hamburger = document.querySelector(".hamburger");

  // Close menu when clicking a nav link
  document.querySelectorAll(".nav-link").forEach(link => {
    link.addEventListener("click", () => {
      menuToggle.checked = false;
    });
  });

  // Close menu when clicking outside
  document.addEventListener("click", function (event) {
    const isMenuOpen = menuToggle.checked;
    const clickedInsideMenu = navContainer.contains(event.target);
    const clickedHamburger = hamburger.contains(event.target);
    const clickedToggle = event.target === menuToggle;

    if (isMenuOpen && !clickedInsideMenu && !clickedHamburger && !clickedToggle) {
      menuToggle.checked = false;
    }
  });
});