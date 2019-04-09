var CookiePolicy = {};

CookiePolicy.toggleCookiePolicy = function toggleCookiePolicy() {
    jQuery("#viewlet-cookiepolicy").slideToggle(500);
};

CookiePolicy.acceptCookiePolicy = function acceptCookiePolicy() {
    var date = new Date();
    date.setFullYear(date.getFullYear() + 1);
    var expires = "; expires="+date.toGMTString();
    document.cookie = "cookie-policy=accepted"+expires+"; path=/";
    CookiePolicy.toggleCookiePolicy();
};

CookiePolicy.deleteCookies = function delete_cookies(domain) {
    var cookie_domain = domain || window.location.hostname;
    cookie_domain = cookie_domain.indexOf('www') === 0 ? cookie_domain.substr(3) : cookie_domain;
    var cookies = document.cookie.split(";");
    var i, cookie, key, cookie_length;
    for (i = 0, cookie_length = cookies.length; i < cookie_length; i += 1) {
        cookie = cookies[i];
        key = cookie.indexOf("=");
        var name = key > -1 ? cookie.substr(0, key) : cookie;
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT" +
            ";domain=" + cookie_domain + ";path=/";
        document.cookie = name + "=;expires=Thu, 01 Jan 1970 00:00:00 GMT" +
            ";path=/";
    }
};

jQuery(function() {
    var btn = document.getElementById("tlspu_submit_button");
    if (!btn) {
        return;
    }

    btn.onclick = function(evt) {
        CookiePolicy.acceptCookiePolicy();
        evt.preventDefault();
    };

    var cookies = document.cookie.split(';');
    var i, c_length;
    for(i=0, c_length = cookies.length; i < c_length; i += 1) {
        if (cookies[i].indexOf("cookie-policy=") !== -1) {
            return;
        }
    }

    setTimeout(CookiePolicy.toggleCookiePolicy, 1000);
});
