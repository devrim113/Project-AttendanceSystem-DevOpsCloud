import { API_PATH_COGNITO, API_SCHEMA, FULL_API_URL, getBearerToken } from "../Helper/static";

/**
 * Constructs a URL with the given parameters, method, and optional body.
 * @param parameters - The parameters to be included in the URL.
 * @param method - The HTTP method to be used for the request.
 * @param body - The optional request body.
 * @returns A function that, when called, sends a fetch request to the constructed URL.
 * @throws An error if 'func' is not present in the parameters.
 */
function get_URL(parameters: { [key: string]: string }, method: string, body?: { [key: string]: string }) {
    // Check if 'func' is in parameters
    if (!('func' in parameters)) {
        throw new Error('func not in parameters');
    }

    let url = new URL(
        FULL_API_URL(API_SCHEMA, API_PATH_COGNITO),
    )
    url.search = new URLSearchParams(parameters).toString();
    console.log(url.toString());
    console.log(body);
    return (() => fetch(url.toString(), {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `${getBearerToken()}`
        },
        body: body === undefined ? undefined : JSON.stringify(body),
    }))
}

/**
 * Creates a teacher record in the system.
 * @param username - The username of the teacher.
 * @param email - The email of the teacher.
 * @returns A Promise that resolves to the result of the API call.
 */
export function create_teacher(username: string, email: string) {
    return get_URL(
        { 
            func: "create_teacher_record" 
        }, 
        "POST", 
        { 
            "email": email,
            "user_name": username
        }
    )
}

