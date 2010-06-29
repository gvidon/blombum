$("#pvg-export area").each(function (i, area) {
	$.get(area.getAttribute("src"),function (data) { area.coords = data; });
});
