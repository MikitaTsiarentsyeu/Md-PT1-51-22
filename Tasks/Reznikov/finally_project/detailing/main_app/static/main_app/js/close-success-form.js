function close_success(){    
    $('.close-success-form').click(function() {
        $('#success-form').fadeOut(800);
        $('html').removeClass('no-scroll');
    })
}

export {close_success}
