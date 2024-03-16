// import { API_SCHEMA, FULL_API_URL, API_PATH_ADMIN, getBearerToken } from "../Helper/static";

// This is a default function to make the call, so that we don't have to repeat the same code for each function
// function get_URL(parameters: { [key: string]: string }, method: string, body?: { [key: string]: string }) {
//     // Check if 'func' is in parameters
//     if (!('func' in parameters)) {
//         throw new Error('func not in parameters');
//     }

//     let url = new URL(FULL_API_URL(API_SCHEMA, API_PATH_ADMIN))
//     url.search = new URLSearchParams(parameters).toString();
//     return (() => fetch(url.toString(), {
//         method: method,
//         headers: {
//             'Content-Type': 'application/json',
//             'Authorization': `${getBearerToken()}`
//         },
//         body: body === undefined ? undefined : JSON.stringify(body),
//     }))
// }

export {}
