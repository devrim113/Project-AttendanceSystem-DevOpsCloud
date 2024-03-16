import { API_PATH_STUDENT, API_SCHEMA, FULL_API_URL, getBearerToken } from "../Helper/static";

// This is a default function to make the call, so that we don't have to repeat the same code for each function
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

export function get_all_courses() {
    return get_URL(
        {
            "func": 'get_all_courses'
        },
        'GET',
        undefined
    )
}

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

interface AttendanceDateRecord {
    [date: string]: AttendanceRecord;
}

interface AttendanceRecord {
    from: string;
    to: string;
    status: 'present' | 'absent' | null;
}

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