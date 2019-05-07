$(function () {
    $('a.action-view-group-info').on('click', function () {
        ModalWorkflow({ url: this.href });
        return false;
    });
});
