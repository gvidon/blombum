var sys = require("sys"),
    http = require("http");

var record_message = function(request, msg) {
	sys.puts(JSON.parse(msg)[0].params.body);
};

http.createServer(function (request, response) {
	var content = "";
	
	request.addListener("body", function(chunk) {
		content += chunk;
	});
	
	request.addListener("complete", function() {
		record_message(request, content);
		response.sendHeader(200, {"Content-Type": "text/plain"});
		response.sendBody("stored message");
		response.finish();
	});
}).listen(8001);
