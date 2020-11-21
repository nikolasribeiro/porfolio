'use strict'

window.addEventListener('load', main);

function main() {
    const MENU_ICON = document.querySelector(".burger");
    const NAVBAR    = document.querySelector(".menubar");

    MENU_ICON.addEventListener("click", ()=>{

        NAVBAR.classList.toggle("change");

    });
}