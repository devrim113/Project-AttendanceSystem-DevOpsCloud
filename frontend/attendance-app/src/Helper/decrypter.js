function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(window.atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
}

function checkValidity(token) {
    const decryptedToken = parseJwt(token)
    return decryptedToken["exp"] > (Date.now()/1000)
}

function generateSimpleUUID() {
    const timestamp = Date.now().toString(36); // Time component
    const randomPart = Math.random().toString(36).substring(2); // Some randomness
  
    return `${timestamp}-${randomPart}`; 
  }


export {parseJwt, checkValidity, generateSimpleUUID}