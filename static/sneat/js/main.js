$('document').ready(function() {
    function loader(btn_id_or_class){
      // when calling the function be sure to add the id (#) or class (.) selector to the params in str ''
      // ex : loader('.classname') or loader('#id')
      var btn = $(btn_id_or_class)
      $(btn).on('click', function() {
      btn.html('<div class="spinner-border" role="status"><span class="visually-hidden">Loading...</span></div>')
   });
  }
  loader('#logout')
  loader('.confimer_action')
  loader('#adduser')
})