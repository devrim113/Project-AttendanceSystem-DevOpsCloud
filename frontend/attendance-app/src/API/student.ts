import { API_PATH_STUDENT, API_SCHEMA, FULL_API_URL, getBearerToken } from "../Helper/static";

/**
 * Constructs a URL with query parameters and returns a function that performs a fetch request.
 * @param parameters - An object containing query parameters.
 * @param method - The HTTP method for the fetch request.
 * @param body - An optional object representing the request body.
 * @returns A function that performs a fetch request with the constructed URL.
 * @throws An error if 'func' is not present in the parameters object.
 */
function get_URL(parameters: { [key: string]: string }, method: string, body?: { [key: string]: string | AttendanceDateRecord }) {
    // Check if 'func' is in parameters
    if (!('func' in parameters)) {
        throw new Error('func not in parameters');
    }

    let url = new URL(
        FULL_API_URL(API_SCHEMA, API_PATH_STUDENT),
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
 * Creates a new student.
 * @param ItemId - The ID of the student item.
 * @param UserName - The username of the student.
 * @param ItemType - The type of the student item.
 * @returns A function that performs a fetch request to create a new student.
 */
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

/**
 * Retrieves the list of students for a specific item.
 * @param ItemId - The ID of the item.
 * @returns A function that performs a fetch request to get the student list.
 */
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

/**
 * Retrieves the courses of a specific student.
 * @param ItemId - The ID of the student.
 * @returns A function that performs a fetch request to get the student's courses.
 */
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

/**
 * Retrieves the course names of a specific student.
 * @param ItemId - The ID of the student.
 * @returns A function that performs a fetch request to get the student's course names.
 */
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

/**
 * Retrieves all courses.
 * @returns A function that performs a fetch request to get all courses.
 */
export function get_all_courses() {
    return get_URL(
        {
            "func": 'get_all_courses'
        },
        'GET',
        undefined
    )
}

/**
 * Enlists a student in a course.
 * @param ItemId - The ID of the item.
 * @param UserId - The ID of the user.
 * @param CourseId - The ID of the course.
 * @returns A function that performs a fetch request to enlist a student in a course.
 */
export function enlist_student_course(ItemId: string, UserId: string, CourseId: string) {
    return get_URL(
        {
            "func": 'enlist_student'
        },
        'PUT',
        {
            "ItemId": ItemId,
            "UserId": UserId,
            "CourseId": CourseId,
            "Attendance": ""
        }
    )
}

/**
 * Retrieves the attendance of a student in a specific course.
 * @param UserId - The ID of the user.
 * @param CourseId - The ID of the course.
 * @returns A function that performs a fetch request to get the student's course attendance.
 */
export function get_student_course_attendance(UserId: string, CourseId: string) {
    return get_URL(
        {
            "func": 'get_student_course_attendance',
            "UserId": UserId,
            "CourseId": CourseId
        },
        'GET',
        undefined
    )
}

/**
 * Represents the attendance record for a specific date.
 */
interface AttendanceDateRecord {
    [date: string]: AttendanceRecord;
}

/**
 * Represents the attendance record for a specific date.
 */
interface AttendanceRecord {
    from: string;
    to: string;
    status: 'present' | 'absent' | null;
}

/**
 * Updates the attendance of a student for a specific course.
 * @param ItemId - The ID of the item.
 * @param Attendance - The attendance record.
 * @param courseId - The ID of the course.
 * @returns A function that performs a fetch request to update the student's attendance.
 */
export function update_attendance(ItemId: string, Attendance: AttendanceDateRecord, courseId: string) {
    return get_URL(
        {
            "func": 'update_attendance'
        },
        'PUT',
        {
            "ItemId": ItemId,
            "Attendance": Attendance,
            "CourseId": courseId
        }
    )
}