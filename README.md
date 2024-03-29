# course-review-portal-backend

This is the backend API for the Course Review Portal. Below, you'll find a list of endpoints along with the supported request verbs, request bodies (wherever required), and example responses.

## Endpoints

### `dept/`

- `GET`: Retrieve a list of all courses.

    Request:
    ```
    GET dept/
    ```

    Response:
    ```
    {
        "departments": [
            {
                "id": 1,
                "name": "CS"
            },
            {
                "id": 2,
                "name": "MA"
            },
            {
                "id": 3,
                "name": "BB"
            },
            {
                "id": 4,
                "name": "ME"
            }
        ]
    }
    ```

- `POST`: Create a new department.

    Request:
    ```
    POST dept/
    Content-Type: application/json

    {
        "name": "<name_of_new_dept>",
    }
    ```
    where ```<name_of_new_dept>``` is a variable. A request of any other formate will fail.

    Response (Success):
    ```
    {
        "success": "Department added",
    }
    ```

    Response (Failure):
    ```
    {
        "error": "Invalid request"
    }
    ```

### `dept/:dept_id`

- *NOTE*: If `dept_id` does not identify any department in the database, the response is:
```
{
    "error": "Department not found"
}
```

- `GET`: Retrieve details of a specific department.

    Request:
    ```
    GET dept/1/
    ```

    Response:
    ```
    {
        "id": 1,
        "name": "CS",
        "courses": [
            {
                "id": 1,
                "code": 105,
                "info": "Graph Theory",
                "ratings": [
                    3.0,
                    3.5
                ],
                "average_rating": 3.25
            },
            {
                "id": 2,
                "code": 108,
                "info": "SSL",
                "ratings": [
                    3.0
                ],
                "average_rating": 3.0
            }
        ]
    }
    ```

- `POST`: Add a new course.

    Request:
    ```
    POST dept/1/
    Content-Type: application/json

    {
        "code": "200",
        "info": "Multiplying 2 digit numbers"
    }
    ```

    Response:
    ```
    {
        "success": "Department updated"
    }
    ```


- `PUT`: Update details of a specific department.

    Request:
    ```
    PUT dept/1/
    Content-Type: application/json

    {
        "name": "ME"
    }
    ```

    Response:
    ```
    {
        "success": "Department updated"
    }
    ```

- `DELETE`: Delete a specific department.

    Request:
    ```
    DELETE department/1/
    ```

    Response:
    ```
    {
        "success": "Department removed"
    }
    ```

### `dept/:dept_id/top_courses`

- `GET`: Retrieve top courses from a specific department

Request:
    ```
    GET dept/94/top_courses
    ```
    
Response:
    ```
    {
        "top_courses": [
            {
                "id": 717,
                "department": 94,
                "code": 103,
                "info": "---INFO OF EE103---",
                "review": "",
                "ratings": [5.0, 3.5, 4.5, 4.5, 3.0, 3.5, 4.5, 5.0, 2.5, 4.5],
                "average_rating": 4.05
            },
            {
                "id": 720,
                "department": 94,
                "code": 106,
                "info": "---INFO OF EE106---",
                "review": "",
                "ratings": [3.0, 5.0, 3.5, 2.5, 4.5, 3.0, 4.0, 4.5, 3.5, 2.0],
                "average_rating": 3.55
            },
            {
                "id": 722,
                "department": 94,
                "code": 108,
                "info": "---INFO OF EE108---",
                "review": "",
                "ratings": [5.0, 5.0, 3.0, 2.5, 1.5, 5.0, 3.5, 2.5, 3.5, 0.0],
                "average_rating": 3.15
            }
        ]
    }
    ```

### `dept/:dept_id/course/:course_id`

- *NOTE*: If `dept_id` does not match a department or if there is not matched course with the ID of `course_id` in the database, the response is:
```
{
    "error": "Course not found"
}
```

- `GET`: Retrieve details of a specific department.

    Request:
    ```
    GET dept/7/course/5
    ```

    Response:
    ```
    {
        "id": 5,
        "department": 7,
        "code": 105,
        "info": "Discrete Structures",
        "ratings": [
            4.5,
            3.0
        ],
        "average_rating": 3.75
    }
    ```


- `POST`: Add a rating to a course.

    Request:
    ```
    PUT dept/1/
    Content-Type: application/json

    {
        "rating": "4.5"
    }
    ```

    Response (Success):
    ```
    {
        "success": "Rating added"
    }
    ```

    Response (If the rating is not valid):
    ```
    {
        "error": "Rating should be between 0 and 5 in steps of 0.5"
    }

- `PUT`: Update a specific course.

    Request:
    ```
    PUT dept/7/course/5
    Content-Type: application/json

    {
        "code": 333,
        "info": "Graph theory"
    }
    ```
    (You need only supply those attributes which you want to change.)

    Response:
    ```
    {
        "success": "Course updated"
    }
    ```

- `DELETE`: Delete a specific course.

    Request:
    ```
    DELETE department/7/course/5
    ```

    Response:
    ```
    {
        "success": "Course removed"
    }
    ```

### `seed/`
- `GET`: Seeds the entire database

    Request:
    ```
    GET seed/
    ```

    Response:
    ```
    {
        "success": "Database seeded"
    }
    ```
