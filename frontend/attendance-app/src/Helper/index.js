import Cookies from 'js-cookie';
function setCookie(name, value, options = { expires: 1, path: '/' }) {
    Cookies.set(name, value, options);
}

function getCookie(name) {
    return Cookies.get(name);
}

export { setCookie, getCookie }