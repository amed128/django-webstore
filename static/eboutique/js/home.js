const  goUpBtn = document.querySelector('.go-up-btn')

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


window.addEventListener('scroll', upBttn);



