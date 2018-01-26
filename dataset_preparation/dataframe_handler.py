import dateutil
import pandas as pd


class DataframeHandler:

    def __init__(self, df):
        self.df = df


    def process(self):
        df = self.df

        for column in df.columns:

            if df[column].dtype == 'int64':
                df[column] = df[column].astype('float')

            if df[column].dtype == 'object':

                # Could be a date
                try:
                    df[column] = pd.to_datetime(df[column])
                    df[column] = df[column].apply(lambda x: dateutil.parser.parse(x))

                except (ValueError, TypeError):
                    pass

                # Could be a currency
                currency_symbols = ['$', '£', '₹']

                try:
                    if df[column].str[0].isin(currency_symbols).all():
                        df[column] = df[column].str.replace('$', '')
                        df[column] = df[column].str.replace('£', '')
                        df[column] = df[column].str.replace('₹', '')
                        df[column] = df[column].str.replace(',', '')
                        df[column] = df[column].astype('float')

                except AttributeError:
                    pass

                # Could be a number

                try:
                    df[column] = df[column].str.strip()
                    df[column] = df[column].str.replace(',', '')
                    df[column] = df[column].astype('float')
                except (AttributeError, ValueError):
                    pass


        return df
