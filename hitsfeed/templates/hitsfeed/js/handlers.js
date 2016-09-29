{% load instant_tags %}

if ( channel == '{% get_staff_channel %}') {
	if (event_class == '__hit__') {
		var hit = data['path']+' '+data['method']+' '+data['ip']
		if ( debug === true) {
			console.log("Hit on "+hit);
		}
		var ua_all = data['user_agent'];
		var length = 35;
		var ua = ua_all.substring(0,length);
		// table
		var content = '<tr><td style="font-weight:bold">'+data['path']+'</td><td>'+data['ip']+' '+data['method']+'</td><td>'+data['user']+'</td></tr>'
		content = content+'<tr><td colspan="3" style="font-size:85%"><i>'+data['user_agent']+'</td></tr>'
		if ( data['referer'] != '' ) {
			content = content+'<tr><td colspan="3" style="font-size:85%"><i>Referer</i>: '+data['referer']+'</td></tr>'
		}
		$('#hitsfeed tbody').after(content);
		if ( startcounter > 25) {
			$('#hitsfeed tr:last').remove();
		}
		else { startcounter++ };
		// activity
		num_events = num_events+1;
		// tree
		function replaceAll(str, find, replace) {
			  return str.replace(new RegExp(find, 'g'), replace);
			}
		var id = replaceAll(data['path'], '/', '---');
		zid = '#'+id;
		displayzone = '#displayzone_'+id;
		$(zid).addClass('activehit');
		$(displayzone).html(data['user']);
		setTimeout(function() {
			$(zid).removeClass('activehit');
			$(zid).addClass('visitedurl');
		}, 1000);
	}
	return false;
}