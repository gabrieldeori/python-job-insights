from src.jobs import read


TABLE_JOB_TYPE = 'job_type'
TABLE_INDUSTRY = 'industry'
TABLE_MAX_SALARY = 'max_salary'
TABLE_MIN_SALARY = 'min_salary'


def filter_jobs_by(jobs, role_name, role):
    return [job for job in jobs if job[role_name] == role]


def get_uniques_strings(path, of_type):
    unique_list = read(path)
    unique_type_list = set()

    for unique in unique_list:
        unique_type = unique[of_type]
        unique_type_list.add(unique_type)
    filtered_list = [unique for unique in unique_type_list if unique != ""]
    return filtered_list


def get_uniques_numbers(path, of_type):
    number_list = read(path)
    number_type_list = []

    for number in number_list:
        number_type = number[of_type]
        if number_type.isnumeric():
            number_type = int(number_type)
            number_type_list.append(number_type)
    return number_type_list


def get_unique_job_types(path):
    job_type_list = get_uniques_strings(path, TABLE_JOB_TYPE)
    return job_type_list


def filter_by_job_type(jobs, job_type):
    return filter_jobs_by(jobs, TABLE_JOB_TYPE, job_type)


def get_unique_industries(path):
    industries_type_list = get_uniques_strings(path, TABLE_INDUSTRY)
    return industries_type_list


def filter_by_industry(jobs, industry):
    return filter_jobs_by(jobs, TABLE_INDUSTRY, industry)


def get_max_salary(path):
    list_max_salary = get_uniques_numbers(path, TABLE_MAX_SALARY)
    max_salary = max(list_max_salary)

    return max_salary


def get_min_salary(path):
    list_min_salary = get_uniques_numbers(path, TABLE_MIN_SALARY)
    min_salary = min(list_min_salary)

    return min_salary


def matches_salary_range(job, salary):
    print(job, salary)
    if TABLE_MIN_SALARY not in job.keys()\
            or TABLE_MAX_SALARY not in job.keys():
        raise ValueError("Algum dos valores não está presente")

    min_salary = job[TABLE_MIN_SALARY]
    max_salary = job[TABLE_MAX_SALARY]
    check_validate = [max_salary, min_salary, salary]

    if not all(isinstance(num, int) for num in check_validate):
        raise ValueError("Algum dos valores não é inteiro")

    if max_salary < min_salary:
        raise ValueError("Salário mínimo menor que o máximo")
    return max_salary >= salary >= min_salary


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
