import React, { useEffect } from 'react';
import { getCookie, setCookie } from '../../Helper';
import { checkValidity } from '../../Helper/decrypter';
import { parseCognitoTokensFromUrl } from '../../Helper/login';
import { bearerCookie, getInformation } from '../../Helper/static';


type RedirectWithTokenProps = {
    children: React.ReactNode
}

/**
 * Renders the RedirectWithToken component.
 * 
 * @param props - The component props.
 * @returns The rendered component.
 */
function RedirectWithToken(props: RedirectWithTokenProps) {
    let { idToken } = parseCognitoTokensFromUrl()
    if(idToken === null) {
        idToken = getCookie(bearerCookie);
    }
    if (idToken && checkValidity(idToken)) {
        const epochTimeExpire: number = getInformation()["exp"]
        const utcString = new Date((epochTimeExpire * 1000)+3600).toUTCString()
        setCookie(bearerCookie, idToken)
    } else {
        window.location.href = 'https://student-attendance-system.auth.eu-central-1.amazoncognito.com/login?response_type=token&client_id=6pnhs85ctml9b9f353b14ui6b4&redirect_uri=https://d5j4m0w9schy1.cloudfront.net/'; 
    }
    return (
    <div>
        {props.children}
    </div>); 
}

export default RedirectWithToken;