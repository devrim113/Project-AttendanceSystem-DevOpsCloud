import { API_PATH_COGNITO, API_SCHEMA, FULL_API_URL } from "../Helper/static";

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
        },
        body: body === undefined ? undefined : JSON.stringify(body),
    }))
}

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

