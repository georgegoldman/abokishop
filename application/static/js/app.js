
x = document.querySelector('#content-box');
y = document.querySelector('#v-pills-tab');
z = document.querySelector('#nav-btn-open');
i = document.querySelector('#nav-btn-close');

var showNav = function() {
    x.style.display = 'none';
    y.style.display = 'block';
    z.style.display = 'none';
    i.style.display = 'block'
}

var hideNav = function() {
    x.style.display = 'block';
    y.style.display = 'none';
    z.style.display = 'block';
    i.style.display = 'none';
}

// var resetNavToggle = function() {
//     x.style.display = "block";
//     y.style.display = "none";
// }

// document.querySelector('#nav-btn').addEventListener('click', navToggle);
// document.getElementsByTagName('body').addEventListener('click', resetNavToggle);

