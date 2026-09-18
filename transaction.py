from dataclasses import dataclass, field
from datetime import date as date_type, datetime

@dataclass
class Transaction:
    id = int
    type = str
    amount : float
    category : str
    date : str = field(default_factory = lambda: datetime.now().strftime('%Y-%m-%d'))
    note : str = ''
    