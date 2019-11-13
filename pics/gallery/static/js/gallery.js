var api_urls = {
  'pictures': 'api/pictures/',
}

function reload_gallery() {
  var user = $('#filter_user')[0].value
  $.ajax({
    url: api_urls['pictures'],
    type: "get",
    data: { 
      format: "json",
      user: user
    },
    success: function(response) {
      $('.picrureBox').remove();
      $.each(response, function(k,v){
        $(
          
        `
        <div class="item picrureBox">
          <div class="image">
            <img src="${v.image_path}" alt="${v.title}" />
          </div>
        <div class="form">
        
        <div class="form-item">
              Owner: ${v.user.username}(${v.user.id}) Pic_id:<a href="${api_urls['pictures']}${v.id}">${v.id}</a>
          </div>
          <div class="form-item">
          <input placeholder="Your note" id="note_${v.id}" type="text" value="${v.note.text}">
          <button href="${api_urls['pictures']}${v.id}" >
          Save note
          </button>
          </div>
          <footer>
            <button href="${api_urls['pictures']}${v.id} class="delete_img delete">Delete</button>
          </footer>
          </div>
          </div>

          `          
          
          ).appendTo('#picturesContainer')
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
  var title = $('#title')[0].value
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
})
 
  $(document).ready(function(){
    reload_gallery()
});
