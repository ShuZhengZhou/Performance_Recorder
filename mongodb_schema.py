from dateutil.parser import parse


def Moniotring_Record(date: str, percentage: float, correct: int, incorrect : int):

    Record = {
    "Date" : parse(date),
    "Subject" : "Monitoring",
    "Percentage" : percentage,
    "Correct" : correct,
    "Incorrect" : incorrect
    }

    return Record

def Multitasking_Record(date: str, percentage: float, triangle: int, calculation: int, duplicate: int):

    Record = {
        "Date" : parse(date),
        "Subject" : "Multitasking",
        "Percentage" : percentage,
        "Triangle" : triangle,
        "Calculation" : calculation,
        "Duplicate" : duplicate
    }

    return Record

def Spatial_Record(date: str, percentage: float, correct: int, incorrect: int):

    Record = {
        "Date" : parse(date),
        "Subject" : "Spatial",
        "Percentage" : percentage,
        "Correct" : correct,
        "Incorrect" : incorrect
    }

    return Record

def Missile_Record(date: str, percentage: float, correct: int):
 
    Record = {
        "Date" : parse(date),
        "Subject" : "Spatial",
        "Percentage" : percentage,
        "Correct" : correct
    }

    return Record