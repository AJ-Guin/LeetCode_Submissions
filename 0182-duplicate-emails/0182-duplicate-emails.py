import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicate_email = person['email'][person['email'].duplicated()]
    return pd.DataFrame({'Email':duplicate_email.unique()})