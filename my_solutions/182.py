import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    res = person.groupby('email')\
    .filter(lambda x: len(x) > 1)\
    .drop_duplicates(subset=['email'])\
    [['email']]
    return res.rename(columns={'email': 'Email'})
