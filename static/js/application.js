$(document).ready(function () {
    $('set_on').click(function () {
        $.post('/toggle_gpio_state/1');
    });
    $('set_off').click(function () {
        $.post('/toggle_gpio_state/0');
    });
});