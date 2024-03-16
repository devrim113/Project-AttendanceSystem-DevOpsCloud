import { API_PATH_COURSE, API_SCHEMA, FULL_API_URL, getBearerToken } from "../Helper/static";

/**
 * Constructs a URL with the given parameters, method, and optional body.
 * @param parameters - The parameters to be included in the URL.
 * @param method - The HTTP method to be used for the request.
 * @param body - The optional request body.
 * @returns A function that, when called, sends a fetch request to the constructed URL.
 * @throws An error if 'func' is not present in the parameters.
 */
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

/**
 * Creates a new course.
 * @param ItemId - The ID of the course item.
 * @param CourseName - The name of the course.
 * @param DepartmentId - The ID of the department the course belongs to.
 * @returns A promise that resolves to the result of the API call.
 */
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

/**
 * Retrieves a course based on the provided ItemId.
 * @param ItemId - The unique identifier of the course.
 * @returns A Promise that resolves to the course data.
 */
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

/**
 * Updates a course with the specified details.
 * @param ItemId - The ID of the course to update.
 * @param CourseName - The new name of the course.
 * @param DepartmentId - The ID of the department the course belongs to.
 * @param Classes - An object containing the classes associated with the course.
 * @returns A Promise that resolves to the updated course.
 */
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