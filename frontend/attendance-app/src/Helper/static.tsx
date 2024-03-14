import { getCookie } from ".";
import { parseJwt } from "./decrypter";

export const bearerCookie = "bearer"
export const getBearerToken = () => getCookie(bearerCookie);

export const getInformation = () => parseJwt(getBearerToken());

// {
//     "at_hash": "hQvywakpWev2rQe1RFglkA",
//     "sub": "e4a6b537-2fa6-4724-8ee2-4c39ab77e032",
//     "cognito:groups": [
//       "Teachers",
//       "Admins",
//       "Students"
//     ],
//     "email_verified": true,
//     "iss": "https://cognito-idp.eu-central-1.amazonaws.com/eu-central-1_jiDMNCeuM",
//     "cognito:username": "e4a6b537-2fa6-4724-8ee2-4c39ab77e032",
//     "aud": "6pnhs85ctml9b9f353b14ui6b4",
//     "event_id": "19e72738-c473-49ee-a379-5858e848c1e7",
//     "token_use": "id",
//     "auth_time": 1710079093,
//     "name": "Ryan Brispat",
//     "exp": 1710082693,
//     "iat": 1710079093,
//     "jti": "67b2e120-4845-4033-96d0-1de3fae08ba7",
//     "email": "ryan.brispat@student.uva.nl"
//   }

// export const getRole = () => getInformation()["cognito:groups"][0];

export const API_URL = "https://i7afcdbeif.execute-api.eu-central-1.amazonaws.com"

export const API_SCHEMA = "/prod"

export const API_PATH_STUDENT = "/student"
export const API_PATH_COURSE = "/course"
export const API_PATH_DEPARTMENT = "/department"
export const API_PATH_TEACHER = "/teacher"
export const API_PATH_ADMIN = "/admin"
export const API_PATH_COGNITO = "/cognito"

export const FULL_API_URL = (scheme: string, path: string) => API_URL + scheme + path