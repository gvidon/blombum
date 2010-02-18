$(document).ready(function() {
	$('.form-row.crossposting_que').hide().after('<div class="form-row">\
		Crosspost URLs <div class="ajaxloader">&nbsp;</div>\
		<ul id="crossposts"></ul><br/>\
	</div>').after('<div class="form-row"><a id="show-services" href="#">Make more crossposts</a></div>');
	
	$.getJSON('/crossposting/urls/7', function(data) {
		$('#crossposts').html('');
		
		if( ! data['urls'])
			$('#crossposts').append('<li>No crossposts made yet</li>');
		else
			for(var i in data['urls'])
				$('#crossposts').append('<li><a href="'+data['urls'][i]+'" target="_blank">'+
					data['urls'][i]+
				'</a></li>');
		
		$('.ajaxloader').hide();
		
		return true;
	});
	
	$('#show-services').click(function() {
		$(this).parent().hide();
		$('.form-row.crossposting_que').show();
		
		return false;
	});
});
