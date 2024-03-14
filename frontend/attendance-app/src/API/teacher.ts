import { API_SCHEMA, FULL_API_URL, API_PATH_TEACHER } from "../Helper/static";

// This is a default function to make the call, so that we don't have to repeat the same code for each function
function get_URL(parameters: { [key: string]: string }, method: string, body?: { [key: string]: string }) {
    // Check if 'func' is in parameters
    if (!('func' in parameters)) {
        throw new Error('func not in parameters');
    }

    let url = new URL(FULL_API_URL(API_SCHEMA, API_PATH_TEACHER))
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

// This is a call to the API to get the teacher's courses
export function get_teacher_course_names(ItemId: string) {
    return get_URL(
        {
            "func": 'get_teacher_course_names',
            "UserId": ItemId,
        },
        'GET',
        undefined
    )
}

export function assign_course_to_teacher(ItemId: string, CourseId: string, UserId: string) {
    return get_URL(
        {
            "func": 'assign_course'
        },
        'PUT',
        {
            "ItemId": ItemId,
            "CourseId": CourseId,
            "UserId": UserId,
        }
    )
}

export function get_all_course_attendance(CourseId: string) {
    return get_URL(
        {
            "func": 'get_course_attendance',
            "CourseId": CourseId,
        },
        'GET',
        undefined
    )
}

// export function create_teacher(email: string, UserName: string) {
//     return get_URL(
//         {
//             "func": 'create_teacher',
//         },
//         'PUT',
//         {
//             "ItemId": email,
//             "UserName": UserName,
//             "ItemType": "Teacher",
//         }
//     )
// }