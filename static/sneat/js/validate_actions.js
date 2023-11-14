$('document').ready(function () {
  function openConfirmModal(on="", action="", message , description) {
    $('#confirmMessage').text(message);
    $('#confirmDescription').text(description);
    $('#confirmButton').on('click', function () {
      switch (on) {
        case 'admin':
          $.get('/sante/admin/' + pk + '/' + action, function (data) {
            location.reload();
          });
          break;
        case 'collect':
          $.get('/sante/admin/' + pk + '/' + action, function (data) {
            location.reload();
          });
        case 'avatar':
          $.get('/sante/profile/avatar/delete', function (data) {
            location.reload();
          });
          break;
        default:
          break;
      }
      $('#confirmModal').modal('hide');
    });
    $('#confirmModal').modal('show');
  }

  $('.delete_admin').on('click', function () {
    pk = $(this).data('id-admin');
    openConfirmModal('admin','delete', 'Etes-vous sûr de vouloir supprimer ?', 'Au lieu de supprimer définitivement l\'utilisateur, vous pouvez simplement le désactiver et le réactiver à tout moment.');
  });

  $('.desable_admin').on('click', function () {
    pk = $(this).data('id-admin');
    openConfirmModal('admin','desable', 'Etes-vous sûr de vouloir désactiver ?', 'L\'utilisateur n\'aura plus accès à son compte.');
  });

  $('.activate_admin').on('click', function () {
    pk = $(this).data('id-admin');
    openConfirmModal('admin','activate', 'Etes-vous sûr de vouloir Activer ?', 'L\'utilisateur aura desormais accès à son compte.');
  });

  $('.delete_collect').on('click', function () {
    pk = $(this).data('id-collect');
    openConfirmModal('collect','delete', 'Etes-vous sûr de retirer ?', 'La collecte  sera definitivement supprimée.');
  });

    $('.confirm_collect').on('click', function () {
    pk = $(this).data('id-collect');
    openConfirmModal('collect','confirm', 'Etes-vous sûr de  vouloir confirmer ?', 'La collecte  sera confirme.');
  });

  $('.post_collect').on('click', function () {
    pk = $(this).data('id-collect');
    openConfirmModal('collect','post', 'Etes-vous sûr de  vouloir publier ?', 'La collecte  sera mise dans la plateforme publique.');
  });

  $('.unpost_collect').on('click', function () {
    pk = $(this).data('id-collect');
    openConfirmModal('collect','unpost', 'Etes-vous sûr de  vouloir depublier ?', 'La collecte  sera retire de la plateforme publique.');
  });

  $('.delete_avatar').on('click', function () {
    openConfirmModal('avatar',message='Cette action est irreversible ?', description='Votre avatar sera definitivment suprimé !');
  });
});
