from io import StringIO
import pandas as pd


def processFiles(mts, redash):

    # mtsIO = StringIO(mts)
    # mtsDF = pd.read_csv(mtsIO, sep=';')

    mtsDF = pd.read_csv(StringIO(mts), sep=';')
    all_columns = list(mtsDF.columns.values)
    allowed_columns = ['Текст сообщения', 'Стоимость', 'Количество сегментов в sms',
                       'Тип пакета', 'Количество sms в пакете при покупке']
    drop_columns = all_columns - allowed_columns

    mtsDF.drop(columns=drop_columns)
    redashDF = pd.read_csv(StringIO(redash), sep=',')

    resultDF = pd.DataFrame()

    return resultDF.to_string()
