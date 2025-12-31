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

  // Handle poem card clicks
  document.querySelectorAll(".poem-card-wrapper").forEach(card => {
    card.addEventListener("click", function (e) {
      e.preventDefault();
      const poemFile = this.dataset.poemFile;
      if (poemFile) {
        $dc.loadPoem(poemFile);
      }
    });
  });
});

(function (global) {
  var dc = {};

  var theAwaitedHtml = "snippets/translation-the-awaited.html";

  // Convenience function for inserting innerHTML for 'select'
  var insertHtml = function (selector, html) {
    var targetElem = document.querySelector(selector);
    targetElem.innerHTML = html;
  };

  // Show loading icon inside element identified by 'selector'.
  var showLoading = function (selector) {
    var html = "<div class='text-center'>";
    html += "<img src='images/ajax-loader.gif'></div>";
    insertHtml(selector, html);
  };

  // Load poem dynamically
  dc.loadPoem = function (poemHtmlPath) {
    showLoading("#display-sec");
    $ajaxUtils.sendGetRequest(
      poemHtmlPath,
      function (responseText) {
        document.querySelector("#display-sec").innerHTML = responseText;
      },
      false
    );
  };

  global.$dc = dc;
})(window);