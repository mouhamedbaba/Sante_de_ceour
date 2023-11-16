$.ajax({
    type: "method",
    url: "localhost:8000/task/update/title/26",
    data: {'title' : 'new title'},
    dataType: "dataType",
    success: function (data) {
        if (success) {
            alert('success')
        } else {
            alert('failed')
        }
    }
});

var scollPosition = window.scrollY || window.pageYOffset || document.documentElement.scrollTop;

window.scrollTo(0, scollPosition)