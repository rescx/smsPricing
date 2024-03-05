import pandas as pd
import os
from collections import defaultdict

df_mts_types = defaultdict(lambda: str, {'Текст сообщения': "string",
                                         "Количество сегментов в sms": "Int64",
                                         "Тип пакета": "string",
                                         "Количество sms в пакете при покупке": "float64"})

df_mts = pd.read_csv(os.getcwd()+"/resources/test_mts_new.csv",
                     sep=";", encoding="cp1251", dtype=df_mts_types)

allowed_columns = ["Текст сообщения", "Стоимость", "Количество сегментов в sms",
                   "Тип пакета", "Количество sms в пакете при покупке"]
df_mts = df_mts[df_mts.columns.intersection(allowed_columns)]

df_mts['Стоимость'] = df_mts['Стоимость'].map(
    lambda x: float(x.replace(",", ".")))

df_mts[["Текст сообщения", "Тип пакета"]] = df_mts[["Текст сообщения",
                                                    "Тип пакета"]].map(lambda x: str(x).lower().replace(" ", ""))


print(df_mts)
