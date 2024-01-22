
var scollPosition = window.scrollY || window.pageYOffset || document.documentElement.scrollTop;


function dargNDrop() {
    console.log('dagen')
    card = $(this).data('card-title')
}

is_modal_oppen = localStorage.getItem('is_modal_oppen')
if (is_modal_oppen === "true") {
    modal_pk = localStorage.getItem('modal_pk')
    var m = $('#'+modal_pk)
    m.show().addClass('show')
}

var path = $('.current-path').val()
console.log(path);


var btn_edit_title = $('.btn-edit-title')
var add_title_form = $('.form-add-title')
var name_edit_container = $('.name-edit-container')
var submit_edit_title_btn = $('.submit-edit-title-btn')
var add_card_button = $('.add-card-button')

function updateTitle(pk, title) {
    $.ajax({
        type: "POST",
        url: "http://localhost:8000/task/update/title/" + pk,
        data: { 'new_title': title },
        // dataType: "script",
        success: function (data) {

        }
    });
}

function addCard(column, title, added_by) {
    $.ajax({
        type: "POST",
        url: "http://localhost:8000/task/card/add/",
        data: { 'title': title, 'column': column, 'added_by': added_by },
        success: function (data) {

        }
    });

    kanban_item = $('<div>').addClass('kanban-item')
    card = $('<div>').addClass('card kanban-item-card hover-actions-trigger bg-holder')
    card.attr('style', 'background-image:url(../../../static/task/assets/img/icons/spot-illustrations/corner-3.png)')
    card_body = $('<div>').addClass('card-body')
    card_postion_relative = $('<div>').addClass('position-relative')
    menu =  $('<div>').addClass('dropdown font-sans-serif')
    button_dropdown = $('<div>').addClass('btn btn-sm btn-falcon-default kanban-item-dropdown-btn hover-actions"').attr("data-bs-toggle", "dropdonw")
    dropdown_menu = $('<div>').addClass('dropdown-menu dropdown-menu-end py-0"')
    card_title = $('<p>').addClass('mb-0 fw-medium font-sans-serif stretched-link cardTitle'+added_by).text(title);



    menu.append(button_dropdown)
    card_postion_relative.append(menu)
    

    card_body.append(card_postion_relative)
    card_body.append(card_title)

    card.append(card_body)

    kanban_item.append(card)

    $('.kanbancontainer'+column).prepend(kanban_item)
}

function editColumn(pk, action, title='Untitled') {
    $.ajax({
        type: "POST",
        url: "http://localhost:8000/task/column/update",
        data: {
            'csrftoken' : 'XT6JMMnUBeYS12X6dzdm59QzJO8PmTPi',
            'pk' : pk,
            'action' : action,
            'title' : title
        },
        success: function (response) {
            console.log(response);
        }
    });
    $.ajax({
        type: "GET",
        url: "http://localhost:8000"+path,
        // data: "data",
        // dataType: "dataType",
        success: function (response) {
            console.log(response);
        }
    });
}


btn_edit_title.on('click', function (e) {
    e.preventDefault(),
        add_title_form.removeClass('d-none')
    name_edit_container.addClass('d-none')
})

submit_edit_title_btn.click(function (e) {
    e.preventDefault();
    input_id = $(this).data('input-id')
    title = $('#' + input_id)
    new_title = title.val();
    if (new_title === "") {
        new_title = "Untitled"
    }
    label_class = $(this).data('label-class')
    label = $('.' + label_class)
    label.html(new_title)
    pk = $(this).data('card-pk')
    updateTitle(pk, new_title)
    add_title_form.addClass('d-none')
    name_edit_container.removeClass('d-none')
});


add_card_button.click(function (e) {
        e.preventDefault();
        input_id = $(this).data('input-id')
        title = $('#'+input_id).val()
        added_by = $(this).data('added-by')
        column = $(this).data('column')
        addCard(column, title, added_by)
    });

setInterval(() => {
    if ($('.modal').hasClass('show')) {

    } else {
        add_title_form.addClass('d-none')
        name_edit_container.removeClass('d-none')
        localStorage.setItem('is_modal_oppen', false)

    }
}, 1000);

let toggle_modal = $('.toggle_modal')
console.log(toggle_modal);

toggle_modal.click(function (e) { 
    modal_pk = $(this).data('modal-pk')
    localStorage.setItem('is_modal_oppen', true)
    localStorage.setItem('modal_pk', modal_pk)

});

var btn_close_modal = $('.btn-close')

btn_close_modal.click(function (e) {
    $('.modal').hide()
    localStorage.setItem('is_modal_oppen', false)
})


var btn_edit_column_title = $('.btn_edit_column')

btn_edit_column_title.click(function (e) {
    e.preventDefault()
    column_pk = $(this).data('column-pk')
    input_id = $(this).data('input-id')
    label_id = $(this).data('label-id')
    btn_save_id = $(this).data('btn-save-id')
    btn_edit_id = $(this).data('btn-edit-id')
    input = $('#'+input_id)
    label = $('#'+label_id)
    btn_save = $('#'+btn_save_id)
    btn_edit = $('#'+btn_edit_id)

    btn_edit.addClass('d-none')
    
    input.removeClass('d-none')
    label.addClass('d-none')

    input.change(function (e) { 
        e.preventDefault();
        title = $(this).val()
        if (title === "") {
            title = "Untitled"
        }
        action = 'update_title'
        editColumn(column_pk, action, title)
        input.addClass('d-none')
        label.removeClass('d-none').text(title)
        btn_edit.removeClass('d-none')
    });

    input.mouseleave(function (e) { 
        e.preventDefault();
        title = $(this).val()
        if (title === "") {
            title = "Untitled"
        }
        action = 'update_title'
        editColumn(column_pk, action, title)
        input.addClass('d-none')
        label.removeClass('d-none').text(title)
        btn_edit.removeClass('d-none')
    });


})

var btn_delete_column = $('.btn-delete-column')
var to_del = []
console.log(to_del);
var delay = 5000
console.log(delay);
btn_delete_column.click(function (e) {
    delay = delay + 1000
    console.log(delay);
    column_pk = $(this).data('column-pk')
    to_del.push(column_pk)
    console.log(to_del);
    action = 'delete'
    column_item_id = $(this).data('column-item-id')
    $('#'+column_item_id).addClass('d-none').removeClass('kanban-column ')
    $('#notifajax').html(`
    <div
          class="bs-toast toast bottom-0 end-0 m-2 show bg-dark"
          role="alert"
          aria-live="assertive"
          aria-atomic="true"
          data-delay="2000"
          style="position:fixed;"
        >

          <div class="toast-body py-2 text-light">
            <div class="d-flex justify-content-between align-items-center">
              <h6 class="text-light">
                liste Suprimée 
            <h6>
              <button class="btn text-white fw-bold shadow-none btn-undo-column-delete">Annuler</button>
            </div>
          </div>
        </div>
    `)
    var undo = false
    
    $('.btn-undo-column-delete').on('click', function () {
        $('#notifajax').html('')
        $('#'+column_item_id).addClass('kanban-column').removeClass('d-none')
        undo = true
        to_del.pop()
        console.log(to_del)
    })

    setTimeout(() => {
        if (undo === true) {
            $('#notifajax').html('')
        } else {
            for (let pk = 0; pk < to_del.length; pk++) {
                editColumn(to_del[pk], action)
            }
        }
        $('#notifajax').html('')
    }, delay);
})

window.scrollTo(0, scollPosition)
