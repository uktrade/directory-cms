$(function () {

    var form = $("form.request-access-form");
    var group_options = form.find("input[name='self_assigned_group']");
    var team_leader_select = form.find("select[name='team_leader']");
    var team_leader_select_wrapper = team_leader_select.closest('li');
    var submit_button = form.find('.button');

    function determine_form_element_interactivity() {
        team_leader_select_wrapper.hide();
        submit_button.attr('disabled', '');

        if (group_options.filter(':checked').length) {
            team_leader_select_wrapper.show();
        }
        if (team_leader_select.val()) {
            submit_button.removeAttr('disabled');
        }
    }

    determine_form_element_interactivity();
    group_options.on('click', determine_form_element_interactivity);
    team_leader_select.on('change', determine_form_element_interactivity);

    $('a.action-view-group-info').on('click', function () {
        ModalWorkflow({ url: this.href });
        return false;
    });
});
