const nav = document.querySelector('.navbar');
let navTop = nav.offsetTop;

const  goUpBtn = document.querySelector('.go-up-btn')

function fixedNav() {
  if (window.scrollY > navTop) {    
    nav.classList.add('fixed');
  } else {
    nav.classList.remove('fixed');    
  }
}

function upBttn() {
  if (scrollY < 500) {
    goUpBtn.hidden = true;
  } else {
    goUpBtn.hidden = false;
    /* setTimeout(function () {
      goUpBtn.hidden = true;
    }, 3000) */
  }

  goUpBtn.addEventListener('click', function () {
    // console.log('go up click')
    if (scrollY) {
      window.scroll(0,0);
    }
  });
}



window.addEventListener('scroll', fixedNav);
window.addEventListener('scroll', upBttn);



