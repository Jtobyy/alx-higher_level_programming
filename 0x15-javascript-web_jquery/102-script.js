window.onload = function() {
    let language_code = $('INPUT#language_code')
    $('INPUT#btn_translate').click(() => {
	$.get('https://www.fourtonfish.com/hellosalut/hello/?lang='+language_code.val(), function(data, textStatus) {
		  $('DIV#hello').html(data)
	      })
    })
}
