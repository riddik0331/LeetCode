import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather['prevDate'] = weather['recordDate'].shift(1)
    weather['prevTemp'] = weather['temperature'].shift(1)

    cond = (weather['recordDate'] - weather['prevDate']).dt.days == 1
    cond &= weather['temperature'] > weather['prevTemp']

    res = weather.loc[cond, ['id']]
    
    return res
