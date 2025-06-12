import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    keep_idx = person.groupby('email')['id'].idxmin()
    drop_idx = person.index.difference(keep_idx)
    person.drop(index=drop_idx, inplace=True)
