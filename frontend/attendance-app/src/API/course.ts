import { API_PATH_COURSE, API_SCHEMA, FULL_API_URL, getBearerToken } from "../Helper/static";

function get_URL(parameters: { [key: string]: string }, method: string, body: { [key: string]: any } | undefined) {
    // Check if 'func' is in parameters
    if (!('func' in parameters)) {
        throw new Error('func not in parameters');
    }

    let url = new URL(
        FULL_API_URL(API_SCHEMA, API_PATH_COURSE),
    )
    url.search = new URLSearchParams(parameters).toString();
    return (async () => fetch(url.toString(), {
        method: method,
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `${getBearerToken()}`
        },
        body: body === undefined ? undefined : JSON.stringify(body),
    }))
}

export function create_course(ItemId: string, CourseName: string, DepartmentId: string) {
    return get_URL(
        {
            "func": 'create_course'
        },
        'PUT',
        {
            "ItemId": ItemId,
            "CourseName": CourseName,
            "DepartmentId": DepartmentId,
            "Classes": "",
        }
    )
}

export function get_course(ItemId: string) {
    return get_URL(
        {
            "func": 'get_course',
            "ItemId": ItemId
        },
        'GET',
        undefined
    )
}

export function update_course(ItemId: string, CourseName: string, DepartmentId: string, Classes: { [key: string]: { [key: string]: string } }) {
    return get_URL(
        {
            "func": 'update_course'
        },
        'POST',
        {
            "ItemId": ItemId,
            "CourseName": CourseName,
            "DepartmentId": DepartmentId,
            "Classes": Classes,
        }
    )
}