function show_login() {
	$("#login-form").show();
	$("#openid-form").hide();
	$("#email").focus();
	return false;
}

function show_openid() {
	$("#login-form").hide();
	$("#openid-form").show();
	$("#id_openid_url").focus();
	return false;
}
