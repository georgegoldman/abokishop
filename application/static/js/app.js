

document.querySelector('#nav-btn').addEventListener('click', function() {
    
    x = document.querySelector('#content-box');
    y = document.querySelector('#v-pills-tab');

    if(x.style.display == "block" || y.style.display == "none"){
        // console.log('connected!');
        x.style.display = "none";
        y.style.display = "block";
    }else{
        // console.log('not connected!')
        x.style.display = "block";
        y.style.display = "none"
    }
        
});