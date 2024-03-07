function setCookie(name, value, options = {}) {
    options = {
        path: '/',
        ...options 
    };

    let updatedCookie = encodeURIComponent(name) + "=" + encodeURIComponent(value);

    for (let optionKey in options) {
        updatedCookie += "; " + optionKey;
        let optionValue = options[optionKey];
        if (optionValue !== true) {
            updatedCookie += "=" + optionValue;
        }
    }

    document.cookie = updatedCookie;
}

function getCookie(name) {
    for(let keyvalue of document.cookie.split(';')) {
        let [cookieName, cookieValue] = keyvalue.split('=');
        if (cookieName.trim() === name) {
            return decodeURIComponent(cookieValue);
        }
    }
    return undefined
}

export { setCookie, getCookie }