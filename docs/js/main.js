$(function() {
  console.log('hello');
  $('a[data-json-path]').each(function() {
    var $this = $(this);
    var json_path = $this.data('json-path');
    var base = location.href.replace(/[^/]+$/, '');
    var raw = base + json_path + '?t=' + new Date().getTime(); // キャッシュバスター
    var json_url = encodeURIComponent(raw);
    var url = 'karabiner://karabiner/assets/complex_modifications/import?url=' + json_url;
    $this.attr('href', url);
  });
});
