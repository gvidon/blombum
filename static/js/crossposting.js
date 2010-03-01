$(document).ready(function() {
	//drop execution on entry add form
	if(window.location.href.search('/admin/blog/post/add') != -1)
		return false;
		
	
	$('.form-row.crossposting_que').hide().after('<div class="form-row">\
		Crosspost URLs <div class="ajaxloader">&nbsp;</div>\
		<ul id="crossposts"></ul><br/>\
	</div>').after('<div class="form-row"><a id="show-services" href="#">Make more crossposts</a></div>');
	
	$.getJSON(window.location.href.replace('/admin/blog/post', '/crossposting/urls'), function(data) {
		$('#crossposts').html('');
		$('.ajaxloader').hide();
		
		if( ! data)
			$('#crossposts').append('<li>No crossposts made yet</li>');
		else
			for(var i in data)
				//paste crosspost URL in list
				if(data[i]['url'])
					$('#crossposts').append('<li><strong>'+data[i]['service']+'</strong>: <a href="'+data[i]['url']+'" target="_blank">'+
						data[i]['url']+
					'</a> '+data[i]['date']+'</li>');
				
				//paste error message
				else if(data[i]['error'])
					$('#crossposts').append('<li><strong>'+data[i]['service']+'</strong>: Error "<i>'+
						data[i]['error']+
					'</i></i> '+data[i]['date']+'</li>');
				
				//paste wait message
				else if(data[i]['error'])
					$('#crossposts').append('<li>in progress...</li>');
		
		return true;
	});
	
	$('#show-services').click(function() {
		$(this).parent().hide();
		$('.form-row.crossposting_que').show();
		
		return false;
	});
});
