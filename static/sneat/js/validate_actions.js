$('document').ready(function () {
  function openConfirmModal(on, action, message, description) {
    $('#confirmMessage').text(message);
    $('#confirmDescription').text(description);
    $('#confirmButton').on('click', function () {
      // Gérez l'action ici
      if (on = 'admin') {
        $.get('/sante/admin/' + pk + '/' + action, function (data) {
          location.reload();
        });
      } else if (on = 'collect') {
        $.get('/sante/collect/' + pk + '/' + action, function (data) {
          location.reload();
        });
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

  // Répétez le même modèle pour les autres cas (collecte, etc.)
});
