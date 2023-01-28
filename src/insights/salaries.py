from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """

    jobs = read(path)
    salaries = []
    for job in jobs:
        salary = job["max_salary"]
        if salary != "invalid" and salary != "":
            salaries.append(int(salary))
    max_salary = max(salaries)
    return max_salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    jobs = read(path)
    salaries = []
    for job in jobs:
        salary = job["min_salary"]
        if salary != "invalid" and salary != "":
            salaries.append(int(salary))
    min_salary = min(salaries)
    return min_salary


def matcher_salary(salary) -> bool:
    types = [int, str]
    if type(salary) not in types:
        return False
    elif isinstance(salary, str) and not salary.isnumeric():
        return False
    return True


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """

    try:
        if not matcher_salary(salary):
            raise ValueError("Invalid Value")
        min = int(job["min_salary"])
        max = int(job["max_salary"])
        if min > max:
            raise ValueError("Invalid Salary Value")
        return min <= int(salary) <= max
    except Exception:
        raise ValueError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
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

    salary_filter = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                salary_filter.append(job)
        except ValueError:
            print(ValueError)
    return salary_filter
