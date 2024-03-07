import React, { useEffect } from 'react';
import { Outlet } from 'react-router';
import { getCookie } from '../../Helper';
import { checkValidity } from '../../Helper/decrypter';
import { parseCognitoTokensFromUrl } from '../../Helper/login';
import { bearerCookie, getInformation } from '../../Helper/static';
import { getImpliedNodeFormatForFile } from 'typescript';

function RedirectWithToken() {
    useEffect(() => {
        const { idToken } = parseCognitoTokensFromUrl() || {idToken : getCookie(bearerCookie)};
        console.log(idToken)
        if (idToken && checkValidity(idToken)) {
            const epochTimeExpire: number = getInformation()["exp"]
            const utcString = new Date((epochTimeExpire * 1000)).toUTCString()
            // Set the id_token as a cookie (adjust options as needed)
            document.cookie = `bearer=${idToken}; expires=; path=/`;
        } else {
            window.location.href = 'https://student-attendance-system.auth.eu-central-1.amazoncognito.com/login?response_type=token&client_id=6pnhs85ctml9b9f353b14ui6b4&redirect_uri=https://d5j4m0w9schy1.cloudfront.net/'; 
        }
    }, []);

    return (
    <div>
        <Outlet/>
    </div>); 
}

export default RedirectWithToken;