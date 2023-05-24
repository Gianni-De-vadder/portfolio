// Fonction pour activer le mode sombre
function enableDarkMode() {
    document.body.classList.add("black");
    document.querySelectorAll("section").forEach(function (section) {
        section.classList.add("black");
    });
    document.querySelectorAll("li").forEach(function (section) {
        section.classList.add("no-bg");
    });
    localStorage.setItem("darkMode", "enabled");
    darkModeToggle.textContent = "light_mode";

}

// Fonction pour désactiver le mode sombre
function disableDarkMode() {
    document.body.classList.remove("black");
    document.querySelectorAll("section").forEach(function (section) {
        section.classList.remove("black");
    });
    document.querySelectorAll("li").forEach(function (section) {
        section.classList.remove("no-bg");
    });
    localStorage.setItem("darkMode", "disabled");
    darkModeToggle.textContent = "dark_mode";
}

// Fonction pour basculer entre le mode sombre et le mode clair
function toggleDarkMode() {
    if (localStorage.getItem("darkMode") === "enabled") {
        disableDarkMode();
    } else {
        enableDarkMode();
    }
}

// Variable pour stocker le dernier timestamp du clic
var lastClickTimestamp = 0;
var darkModeToggle = document.getElementById("dark-mode-toggle");


// Vérifier l'état du mode sombre lors du chargement de la page
document.addEventListener("DOMContentLoaded", function () {
    if (localStorage.getItem("darkMode") === "enabled") {
        enableDarkMode();
    } else {
        disableDarkMode();
    }
});
