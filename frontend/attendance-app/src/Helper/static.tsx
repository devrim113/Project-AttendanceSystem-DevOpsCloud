import { getCookie } from ".";
import { parseJwt } from "./decrypter";

export const bearerCookie = "bearer"
export const getBearerToken = () => getCookie(bearerCookie);

export const getInformation = () => parseJwt(getBearerToken());