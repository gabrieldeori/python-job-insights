from functools import lru_cache
import csv


@lru_cache
def read(path):
    try:
        with open(path) as archive:
            jobs_csv = csv.DictReader(archive, delimiter=",", quotechar='"')
            jobs_list = [job for job in jobs_csv]
            return jobs_list
    except OSError:
        print('Algo deu errado')
        return False
