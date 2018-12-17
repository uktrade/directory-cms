function simplemdeAttach(id) {
        var mde = new SimpleMDE({
            element: document.getElementById(id),
            autofocus: false,
        });
        mde.render();

        mde.codemirror.on("change", function(){
            $('#' + id).val(mde.value());
        });
    }


// Refresh the markdown entry field when the tab buttons are clicked.
// This works around a problem where CodeMirror cannot determine it's height
// if it is hidden. Tab contents are of course hidden before they are clicked.
// Unless this is done the markdown entry field will appear empty until clicked.
(function() {

    var checkExist = setInterval(function() {
        if (document.getElementsByClassName('tab-nav')) {
            clearInterval(checkExist);
            $('.tab-nav').on('shown.bs.tab', refreshMarkdownFields);
        }
    }, 100);

    function refreshMarkdownFields(event) {
        var id = event.target.getAttribute('href').replace('#', '');
        var tabContent = document.getElementById(id);
        var codeElements = tabContent.getElementsByClassName('CodeMirror');
        for (var j = 0; j < codeElements.length; j++) {
            var codeElement = codeElements[j];
            codeElement.CodeMirror.refresh();
        }
    }

})();
