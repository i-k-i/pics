var api_urls = {
  'pics_list': 'api/pictures/list',
  'pics': 'api/pictures/',
}





function update_pictures() {
  $.ajax({
    url: api_urls['pics_list'],
    type: "get",
    data: { 
      format: "json",
    },
    success: function(response) {
      $.each(response, function(k,v){
        $(`<div className="image">
          <img src='${v.image_path}' alt=${v.title}/>
          <h4>${v.title}
          </h4>
          </div>`).appendTo('#picturesContainer')
      })

    },
    error: function(xhr) {
      //Do Something to handle error
    }
})};

$('#apply_filter').on('click', function() {update_pictures()});

$(document).ready(function(){update_pictures()})