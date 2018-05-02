$(function() {

    var errorSections = {};

    $('.required-for-language').each(function(index, element) {
        element = $(element);
        if (!element.val()) {
            var parentSection = $(element).closest('section');
            var id = parentSection.attr('id');
            errorSections[id] = (errorSections[id] || 0) + 1;
        }
    });

    for (var index in errorSections) {
        $('.tab-nav a[href="#' + index + '"]').addClass('required-for-language').attr('data-count', errorSections[index]);
    }
})
