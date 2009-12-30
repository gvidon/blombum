function form_close() {
	$("#login-form").hide();
	$("#openid-form").hide();
	$("#login-close").hide();
    return false;
}

function show_login() {
	$("#login-form").show();
	$("#openid-form").hide();
	$("#login-close").show();
    $("#login-form #email").focus();
    return false;
}

function show_openid() {
	$("#login-form").hide();
	$("#openid-form").show();
	$("#login-close").show();
    $("#openid-form #id_openid_url").focus();
    return false;
}
