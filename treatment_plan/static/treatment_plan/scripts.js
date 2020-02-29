$( document ).ready( function()
{
    // Enable bootstrap tooltips
    $(function () 
    {
        $('[data-toggle="tooltip"]').tooltip()
    })

    // change id param based on client presentation
    $("#clientPresentation").change(function()
    {
        var clientPresentationId = $(this).find(":selected").attr("val");
        var params = new URLSearchParams(location.search);
        params.set("id", clientPresentationId);
        window.location.search = params.toString();
    });

    // Clipboard button. Copy labels and options to clipboard
    $("#clipboardButton").on('click', function()
    {
        var copiedString = '';
        $( ".treatment" ).each(function( index ) 
        {
            if ( $(this).is( "select" ) && $(this).val() != null)
            {
                copiedString = copiedString.concat($(this).val());
                copiedString = copiedString.concat("\r\n");
            }
            else
            {
                copiedString = copiedString.concat($(this).text());
            }
            copiedString = copiedString.concat("\r\n");
        });

        // create temporary area to copy from
        var $temp = $("<textarea>");
        $("body").append($temp);
        $temp.val(copiedString).select();
        document.execCommand("copy");
        $temp.remove();

        $(this).attr('title', 'Copied!')
        .tooltip('_fixTitle')
        .tooltip('show');

    });

    $("#clipboardButton").on("mouseout",function()
    {
        $(this).attr('title',"Copy to clipboard").tooltip('_fixTitle').tooltip('show');
    });
});