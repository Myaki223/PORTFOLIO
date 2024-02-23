function changebg(){
    var navbar = document.getElementById('mainNav');
    var scrollValue = window.scrollY;
   if (scrollValue < 150){
    navbar.classList.remove('bgColor');
   } else{
    navbar.classList.add('bgColor');
   }
}

window.addEventListener('scroll', changebg);