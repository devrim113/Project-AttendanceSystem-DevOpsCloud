import { API_PATH_STUDENT, API_SCHEMA, FULL_API_URL } from "../Helper/static";

// This is a default function to make the call, so that we don't have to repeat the same code for each function
function get_URL(parameters: { [key: string]: string }, method: string, body?: { [key: string]: string }) {
    // Check if 'func' is in parameters
    if (!('func' in parameters)) {
        throw new Error('func not in parameters');
    }

    let url =  new URL(
        FULL_API_URL(API_SCHEMA, API_PATH_STUDENT),
    )
    url.search = new URLSearchParams(parameters).toString();
    return (() => fetch(url.toString(), {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: body === undefined ? undefined : JSON.stringify(body),
    }))
}

// This is a call to the API to get the student's courses
export function create_student(ItemId: string, UserName: string, ItemType: string) {
    return get_URL(
        {
            "func": 'create_student'
        }, 
        'PUT',
        {
            "ItemId": ItemId,
            "UserName": UserName,
            "ItemType": ItemType
        }
    )
}

export function get_student_list(ItemId: string) {
    return get_URL(
        {
            "func": 'get_student',
            "ItemId": ItemId
        }, 
        'GET',
        undefined
    )
}

export function get_student_courses(ItemId: string) {
    return get_URL(
        {
            "func": 'get_student_courses',
            "UserId": ItemId
        }, 
        'GET',
        undefined
    )
}

export function get_student_course_names(ItemId: string) {
    return get_URL(
        {
            "func": 'get_student_course_names',
            "UserId": ItemId
        }, 
        'GET',
        undefined
    )
}