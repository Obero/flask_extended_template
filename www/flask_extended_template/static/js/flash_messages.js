/**
 * Created by Obero on 22/07/2015.
 */

// Make the flash messages disappear after a while
$(function()
{
    var flash_msg = $('.floating-message');
    if (flash_msg.length > 0)
    {
        setTimeout(function()
        {
            flash_msg.fadeOut(2000);
        }, 3000);
    }
});
