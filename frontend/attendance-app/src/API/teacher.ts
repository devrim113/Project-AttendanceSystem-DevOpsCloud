import { API_SCHEMA, FULL_API_URL, API_PATH_TEACHER, getBearerToken } from "../Helper/static";

// This is a default function to make the call, so that we don't have to repeat the same code for each function
/**
 * Constructs a URL with the given parameters, method, and optional body.
 * @param parameters - The parameters to be included in the URL.
 * @param method - The HTTP method to be used for the request.
 * @param body - The optional body to be included in the request.
 * @returns A function that, when called, sends a fetch request to the constructed URL.
 * @throws An error if 'func' is not present in the parameters.
 */
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
            'Authorization': `${getBearerToken()}`
        },
        body: body === undefined ? undefined : JSON.stringify(body),
    }))
}


/**
 * Retrieves the course names associated with a teacher.
 * @param ItemId - The ID of the teacher.
 * @returns A Promise that resolves to the course names.
 */
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

/**
 * Assigns a course to a teacher.
 * 
 * @param ItemId - The ID of the item.
 * @param CourseId - The ID of the course.
 * @param UserId - The ID of the user.
 * @returns A Promise that resolves to the result of the API call.
 */
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

/**
 * Retrieves the attendance data for a specific course.
 * @param CourseId - The ID of the course to retrieve attendance data for.
 * @returns A Promise that resolves to the attendance data for the specified course.
 */
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