document.addEventListener("DOMContentLoaded",()=>{

    const sidebar = document.querySelector(".sidebar");
    const closeBtn = document.querySelector(".cancel");
    const blur = document.querySelector(".blur");
    const menuBtn = document.querySelector(".hb");
    menuBtn.addEventListener("click",()=>{

        sidebar.classList.add("active");
        blur.classList.add("active");

    });

    closeBtn.addEventListener("click",()=>{
        sidebar.classList.remove("active");
        blur.classList.remove("active");
    });

    blur.addEventListener("click",()=>{
        sidebar.classList.remove("active");
        blur.classList.remove("active");
    });
});