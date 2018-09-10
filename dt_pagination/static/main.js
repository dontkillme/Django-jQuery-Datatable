function init() {
  $('table').DataTable({
    "processing": true,
    "serverSide": true,
    "ajax": {
      "url": "/page/",
      "type": "POST",
      "data": {"page": 0},
    }
  })
}

$(window).load(init);