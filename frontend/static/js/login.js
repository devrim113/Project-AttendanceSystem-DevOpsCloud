function setBearerTokenInCookies(token) {
    if (token) {
        document.cookie = `bearer_token=${token};path=/`;
        return true
    }
    return false
}

function parseCognitoTokensFromUrl() {
    const url = window.location.href;
    const hashFragment = url.split('#')[1]; // Get the part after '#'
    const urlParams = new URLSearchParams(hashFragment);
  
    const idToken = urlParams.get('id_token');
    const accessToken = urlParams.get('access_token');
    const expiresIn = urlParams.get('expires_in'); 
    const tokenType = urlParams.get('token_type'); 
  
    return {
      idToken,
      accessToken,
      expiresIn,
      tokenType
    };
  }
