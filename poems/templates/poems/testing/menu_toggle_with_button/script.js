  document.addEventListener("DOMContentLoaded", function () {
    const toggleButton = document.getElementById("menu-toggle");
    const navContainer = document.querySelector(".nav-links-container");

    toggleButton.addEventListener("click", () => {
      navContainer.classList.toggle("open");
    });

    // Optional: close menu when clicking outside
    document.addEventListener("click", (event) => {
      if (
        !navContainer.contains(event.target) &&
        !toggleButton.contains(event.target)
      ) {
        navContainer.classList.remove("open");
      }
    });
  });

  document.querySelectorAll('.nav-link').forEach(link => {
  link.addEventListener('click', () => {
    document.getElementById('menu-toggle').checked = false;
  });
});
