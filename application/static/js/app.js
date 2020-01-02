
x = document.querySelector('#content-box');
y = document.querySelector('#v-pills-tab');

var navToggle = function() {
    if(x.style.display == 'block' && y.style.display == 'none'){
        console.log('connected!');
        x.style.display = "none";
        y.style.display = "block";
    }else{
        console.log('not connected!')
        x.style.display = "block";
        y.style.display = "none";
    }
}

// var resetNavToggle = function() {
//     x.style.display = "block";
//     y.style.display = "none";
// }

document.querySelector('#nav-btn').addEventListener('click', navToggle);
// document.getElementsByTagName('body').addEventListener('click', resetNavToggle);

