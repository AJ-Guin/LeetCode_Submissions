import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    consecutive = logs[
        (logs['num'] == logs['num'].shift(1)) &
        (logs['num'] == logs['num'].shift(2))
    ]
    return pd.DataFrame(
        {'consecutiveNums': consecutive['num'].unique()}
    )