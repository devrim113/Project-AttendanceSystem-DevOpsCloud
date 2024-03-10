import { API_PATH_COURSE, API_SCHEMA, FULL_API_URL } from "../Helper/static";

function get_URL(parameters: { [key: string]: string },method: string, body: { [key: string]: any } | undefined) {
    // Check if 'func' is in parameters
    if (!('func' in parameters)) {
        throw new Error('func not in parameters');
    }

    let url =  new URL(
        FULL_API_URL(API_SCHEMA, API_PATH_COURSE),
    )
    url.search = new URLSearchParams(parameters).toString();
    return ( async () => fetch(url.toString(), {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: body === undefined ? undefined : JSON.stringify(body),
    }))
}

export function create_course(ItemId: string, CourseName: string, ItemType: string, DepartmentId: string, Classes: { [key: string]: { [key: string]: string } }) {
    return get_URL(
        {
            "func": 'create_course'
        }, 
        'PUT',
        {
            'ItemId': '1',
            'CourseName': 'Math',
            'ItemType': 'Course',
            'DepartmentId': '1',
            'Classes': {
                '2022-01-01': {
                    'from': '09:00',
                    'to': '12:00'
                },
                '2022-01-02': {
                    'from': '09:00',
                    'to': '12:00'
                }
            }
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