// Extracted from simplemde source:
// https://github.com/sparksuite/simplemde-markdown-editor/blob/6abda7ab68cc20f4aca870eb243747951b90ab04/src/js/simplemde.js#L791-L822
function _replaceSelection(cm, active, startEnd, url) {
    if (
        /editor-preview-active/.test(cm.getWrapperElement().lastChild.className)
    )
        return;

    var text;
    var start = startEnd[0];
    var end = startEnd[1];
    var startPoint = cm.getCursor('start');
    var endPoint = cm.getCursor('end');
    if (url) {
        end = end.replace('#url#', url);
    }
    if (active) {
        text = cm.getLine(startPoint.line);
        start = text.slice(0, startPoint.ch);
        end = text.slice(startPoint.ch);
        cm.replaceRange(start + end, {
            line: startPoint.line,
            ch: 0,
        });
    } else {
        text = cm.getSelection();
        cm.replaceSelection(start + text + end);

        startPoint.ch += start.length;
        if (startPoint !== endPoint) {
            endPoint.ch += start.length;
        }
    }
    cm.setSelection(startPoint, endPoint);
    // Not entirely sure why this is necessary! Prevents a stacktrace from jQuery when putting focus back into the editor.
    setTimeout(() => {
        cm.focus();
    }, 1);
}

const windowPrompt = window.prompt;

const OVERRIDE_TEXT = 'windowPromptOverride';

const windowPromptOverride = (callback, text) => {
    const shouldOverride = text === OVERRIDE_TEXT;

    if (shouldOverride) {
        callback();
    } else {
        return windowPrompt(text);
    }
}

function openLinkChooser(mde) {
    const workflow = window.ModalWorkflow({
        url: window.chooserUrls.pageChooser,
        urlParams: {
            page_type: 'wagtailcore.page',
            allow_external_link: true,
            allow_email_link: true,
            // TODO Could be nice to implement this.
            link_text: '',
        },
        onload: window.PAGE_CHOOSER_MODAL_ONLOAD_HANDLERS,
        responses: {
            pageChosen: (data) => {
                const isPage = !!data.id;
                const href = isPage ? `slug:${data.slug}` : data.url;
                _replaceSelection(
                    mde.codemirror,
                    mde.getState().link,
                    ['[', '](#url#)'],
                    href,
                );
                workflow.close();
            },
        },
        // TODO Add basic error handling.
        onError: () => {
            window.alert('Error');
        },
    });
}

function simplemdeAttach(id) {
    var mde = new SimpleMDE({
        element: document.getElementById(id),
        promptURLs: true,
        autofocus: false,
    });
    mde.options.promptTexts = {
        link: OVERRIDE_TEXT,
    };
    mde.render();

    mde.codemirror.on('change', function() {
        $('#' + id).val(mde.value());
    });

    // TODO Make sure this is compatible with multiple instances of SimpleMDE on the page.
    window.prompt = windowPromptOverride.bind(null, openLinkChooser.bind(null, mde));
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
