import { getCookie } from ".";
import { parseJwt } from "./decrypter";

export const isProd = true

export const bearerCookie = "bearer"
export const getBearerToken = () => getCookie(bearerCookie);

export const getInformation = () => parseJwt(getBearerToken());

export const API_URL = "https://i7afcdbeif.execute-api.eu-central-1.amazonaws.com"

export const API_SCHEMA = "/prod"

export const API_PATH_STUDENT = "/student"
export const API_PATH_COURSE = "/course"
export const API_PATH_DEPARTMENT = "/department"
export const API_PATH_TEACHER = "/teacher"
export const API_PATH_ADMIN = "/admin"
export const API_PATH_COGNITO = "/cognito"

export const FULL_API_URL = (scheme: string, path: string) => API_URL + scheme + path


export const cognitoURL =  `https://student-attendance-system.auth.eu-central-1.amazoncognito.com/login?response_type=token&client_id=6pnhs85ctml9b9f353b14ui6b4&redirect_uri=${isProd ? "https://d5j4m0w9schy1.cloudfront.net/" : "http://localhost:3000"}`
