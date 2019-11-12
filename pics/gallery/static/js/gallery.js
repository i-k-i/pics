var api_urls = {
  'pictures': 'api/pictures/',
}

function reload_gallery() {
  $.ajax({
    url: api_urls['pictures'],
    type: "get",
    data: { 
      format: "json",
    },
    success: function(response) {
      $('.picrureBox').remove();
      $.each(response, function(k,v){
        $(`<div class="picrureBox">
            <img src='${v.image_path}' alt=${v.title}/>
            <h4>${v.id}</h4>
            Your note: <input id="note_${v.id}" type = "text" value="${v.note.text}"><button href="${api_urls['pictures']}${v.id}" class="delete_img">Save note</button>
            <ul>
              <li><a href="${api_urls['pictures']}${v.id}">Details</a></li>
              <li><button href="${api_urls['pictures']}${v.id}" class="delete_img">Delete</button></li>
            <ul>
          </div>`).appendTo('#picturesContainer')
      })

    },
    error: function(xhr) {
      console.log(xhr)
    }
})};

$('#apply_filter').on('click', function() {reload_gallery()});


$('.upload_btn').on('click', function() {
  var fd = new FormData(); 
  var files = $('#image_path')[0].files[0];
  var title = $('#title')[0]
  var csrftoken = $("[name=csrfmiddlewaretoken]")[0].value
  fd.append('image_path', files);
  fd.append('title', title)
  fd.append('csrfmiddlewaretoken', csrftoken)
  $.ajax({
    url: api_urls['pictures'], 
    type: 'post', 
    data: fd, 
    contentType: false, 
    processData: false, 
    success: function(response){ 
      if(response != 0){ 
        alert('file uploaded');
        $('#upload_form').trigger('reset')
        reload_gallery()
      } 
      else{ 
        alert('file not uploaded'); 
      } 
    }, 
    
  })
});

// $('.delete_img').click(function(){
//   console.log(123)
// });


$('#apply_filter').on('click', function(){
  
})

$(document).ready(function(){
  reload_gallery()
});
