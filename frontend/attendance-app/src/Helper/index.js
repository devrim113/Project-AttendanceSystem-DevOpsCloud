import Cookies from 'js-cookie';
function setCookie(name, value, options = { expires: 1, path: '/' }) {
    console.log(document.cookie)
    Cookies.set(name, value, options);
    console.log(document.cookie)
}

function getCookie(name) {
    return Cookies.get(name);
}

export { setCookie, getCookie }