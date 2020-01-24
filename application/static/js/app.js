
x = document.querySelector('#v-pills-tabContent');
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

var edit_form = function() {
  i = document.querySelector('#update_info');
  j = document.querySelector('#ebtn');
  k = document.querySelector('#cbtn');
  i.style.display = 'block';
  j.style.display = 'none';
  k.style.display = 'block';
}

var close_edit_form = function() {
  a = document.querySelector('#update_info');
  b = document.querySelector('#cbtn');
  c = document.querySelector('#ebtn');
  a.style.display = 'none';
  b.style.display = 'none';
  c.style.display = 'block';


}

// var resetNavToggle = function() {
//     x.style.display = "block";
//     y.style.display = "none";
// }

// document.querySelector('#nav-btn').addEventListener('click', navToggle);
// document.getElementsByTagName('body').addEventListener('click', resetNavToggle);
