from src.sorting import sort_by


f_jobs = [
        {
            'id': 1,
            'min_salary': 8000,
            'max_salary': 17000,
            'date_posted': '2023-05-04',
        },
        {
            'id': 2,
            'min_salary': 18000,
            'max_salary': 26000,
            'date_posted': '2025-05-04',
        },
        {
            'id': 3,
            'min_salary': 27000,
            'max_salary': 35000,
            'date_posted': '2027-05-04',
        },
        {
            'id': 4,
            'min_salary': 3500,
            'max_salary': 7000,
            'date_posted': '2022-05-04',
        },
]


criterias_response = {
        "min_salary": [f_jobs[3], f_jobs[0], f_jobs[1], f_jobs[2]],
        "max_salary": [f_jobs[2], f_jobs[1], f_jobs[0], f_jobs[3]],
        "date_posted": [f_jobs[3], f_jobs[0], f_jobs[1], f_jobs[2]],
    }


def test_sort_by_criteria():
    assert sort_by(f_jobs, "min_salary") == criterias_response["min_salary"]
    assert sort_by(f_jobs, "max_salary") == criterias_response["max_salary"]
    assert sort_by(f_jobs, "date_posted") == criterias_response["date_posted"]
