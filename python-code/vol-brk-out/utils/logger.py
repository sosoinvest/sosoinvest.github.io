import pandas as pd


class Logger:
    """
    Logger is logging the trading data.
    """
    def __init__(self):
        """
        data_dict: [Dictoinary], trading data storagy
        """
        self.data_dict = {}

    def log_data(self, key, data):
        """
        Log data
        :param key: Key to store in the data dictionary
        :param data: Data matching with the key
        :return:
        """
        if key in self.data_dict.keys():
            self.data_dict[key].append(data)
        else:
            self.data_dict[key] = [data]

    def save_data(self, filename):
        """
        Converts the data dictionary into a dataframe and save the dataframe as a csv file.
        :param filename: Name of the file to save.
        :return:
        """
        df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in self.data_dict.items()]))
        df.to_csv(filename)

    def print_in_dataframe(self):
        """
        Converts the data into a dataframe and prints it.
        :return:
        """
        df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in self.data_dict.items()]))
        print(df)
