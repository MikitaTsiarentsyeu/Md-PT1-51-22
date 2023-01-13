// $(document).ready(function() {
function popup(){    
    $('.header_button-popup').click(function(e) {
        e.preventDefault();
        $('.popup-bg').fadeIn(800);
        $('html').addClass('no-scroll');
    });

    $('.close-popup').click(function() {
        $('.popup-bg').fadeOut(800);
        $('html').removeClass('no-scroll');
        document.getElementById('select-time').style.display = 'none';
        document.getElementsByClassName("pressed")[0].className = document.getElementsByClassName("pressed")[0].className.replace(" pressed", "")
    })

}
// });

export {popup}
