function setBearerTokenInCookies() {
    const urlParams = new URLSearchParams(window.location.search);
    const token = urlParams.get('token');
    if (token) {
        document.cookie = `bearer_token=${token}; path=/`;
    }
}