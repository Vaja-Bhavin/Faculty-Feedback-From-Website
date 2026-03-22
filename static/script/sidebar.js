document.addEventListener("DOMContentLoaded", () => {
    const hb = document.querySelector(".hb");
    const sb = document.querySelector(".sidebar");
    const cl = document.querySelector(".cancel");
    const blur = document.querySelector(".blur")

    hb.addEventListener("click", () => {
        sb.classList.add("active");
        blur.style.display="block";
    });

    cl.addEventListener("click", () => {
        sb.classList.remove("active");
        blur.style.display="none";
    });
});