from dataclasses import dataclass
from datetime import date as date_type, datetime

@dataclass
class Expenses:
    id = int
    type = str
    amount : float
    category : str
    date : str = str(datetime.now)
    note : str
    