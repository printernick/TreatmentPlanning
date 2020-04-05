$(document).ready(function () {
    // Enable bootstrap tooltips
    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    })

    // change id param based on client presentation
    $("#clientPresentation").change(function () {
        var clientPresentationId = $(this).find(":selected").attr("val");
        var params = new URLSearchParams(location.search);
        params.set("id", clientPresentationId);
        window.location.search = params.toString();
    });

    // Clipboard button. Copy labels and options to clipboard
    $("#clipboardButton").on('click', function () {
        var copiedString = '';
        $(".selectpicker").each(function (index) {

            //Add labels
            copiedString += $(this).prop("labels")[0].textContent + "\r\n";

            //Add each selected option
            var selectedOptions = $(this).prop("selectedOptions");
            if (selectedOptions.length == 0)
            {
                copiedString += "\r\n";
            }
            else
            {
                
                //Loop through in case of multiple selected options
                $(selectedOptions).each(function (index) {
                    copiedString += $(this)[0].textContent + "\r\n";
                });
            }

            //Extra line after each section
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

    $("#clipboardButton").on("mouseout", function () {
        $(this).attr('title', "Copy to clipboard").tooltip('_fixTitle').tooltip('show');
    });
});