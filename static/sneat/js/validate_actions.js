$('document').ready(function(){

    function actions_admin(button_modal_class, button_confirm_class, action) {
    var admin_to_action = null;
    $(button_modal_class).on('click', function(){
      admin_to_action = $(this).data('id-admin')
    });

    $(button_confirm_class).on('click', function(){
      $.get('/sante/actions/' + admin_to_action + '/' + action, function(data){
        location.reload();
      });
    });
    }
    actions_admin('.delete_admin', '.confimer_action', 'delete')
    actions_admin('.desable_admin', '.confimer_action', 'desable')

    function actions_collect(button_modal_class, button_confirm_class, action) {
      var collect_to_action = null;
      $(button_modal_class).on('click', function(){
        collect_to_action = $(this).data('id-collect')
      });
  
      $(button_confirm_class).on('click', function(){
        $.get('/sante/collect/' + collect_to_action + '/' + action, function(data){
          location.reload();
        });
      });
      }
      actions_collect('.confirm_collect', '.confimer_confirm_collect', 'confirm')
      actions_collect('.delete_collect', '.confimer_delete_collect', 'delete')
      actions_collect('.post_collect', '.confimer_post_collect', 'post')
      actions_collect('.unpost_collect', '.confimer_unpost_collect', 'unpost')
    
  })