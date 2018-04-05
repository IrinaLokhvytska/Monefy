import pandas as pd

class FileParse:
    def read_from_file(self, path):
        return pd.read_csv(path)

    def get_balance(self, data):
        df = pd.DataFrame(data)
        amount = self.__replace_space(df['amount'])
        result = self.__convert_amount_2_float(amount).sum()
        return result

    def __replace_space(self, amount):
        return amount.apply(lambda x: x.replace('\xa0', ''))

    def __convert_amount_2_float(self, amount):
        return pd.to_numeric(amount)


if __name__ == '__main__':
    file_parser = FileParse()
    data = file_parser.read_from_file('Monefy.Data.csv')
    print(file_parser.get_balance(data))