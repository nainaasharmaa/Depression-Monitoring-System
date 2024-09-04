let subMenu = document.getElementById("subMenu");
let userBitmoji = document.querySelector(".user-bitmoji");

function toggleMenu() {
    if (subMenu.classList.contains("open-menu")) {
        // If submenu is already open, close it
        subMenu.classList.remove("open-menu");
        // Remove the event listener when submenu is closed
        document.body.removeEventListener("click", closeMenuOutside);
    } else {
        // If submenu is closed, open it
        subMenu.classList.add("open-menu");
        // Add an event listener to close the submenu when clicking outside it
        document.body.addEventListener("click", closeMenuOutside);
    }
}

function closeMenuOutside(event) {
    // Check if the clicked element is not within the submenu or the user bitmoji
    if (!subMenu.contains(event.target) && event.target !== userBitmoji) {
        // If clicked outside the submenu, close it
        subMenu.classList.remove("open-menu");
        // Remove the event listener after closing the submenu
        document.body.removeEventListener("click", closeMenuOutside);
    }
}
