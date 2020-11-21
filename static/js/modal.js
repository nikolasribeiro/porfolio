'use strict'

window.addEventListener('load', main);

function main(){
    
    const toggle = (name_class)=>{
        document.querySelector(".modal .modal-" + name_class).classList.toggle("hide");
    };
    
    document.querySelector(".close").addEventListener("click", toggle);

    
    /*Selecting all the different modals*/
    document.querySelector(".read-more").addEventListener("click", toggle);




};