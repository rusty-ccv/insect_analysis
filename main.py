import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
# import matplotlib.pyplot as plt
import logging

#setup logging
logging.basicConfig(filename='debug.log', level=logging.DEBUG)

# Project to run two-way ANOVA and plot results
class CsvReader:
    def __init__(self, file):
        self.file = file

    def read(self):
        try:
            csv_data = pd.read_csv(self.file)
            logging.info(f'Reading file: {self.file}')
            return csv_data
        except FileNotFoundError as e:
            logging.error(f'Error: {e}{self.file}')
            raise FileNotFoundError(f'Error: {e}')
        except Exception as e:
            logging.error(f'Error: {e}')
            raise Exception(f'Error: {e}')


class DataAnalysis:
    def __init__(self, csv_data, alpha=0.05):
        self.csv_data = csv_data
        self.alpha = alpha
        self.two_way_anova_result = None

    def two_way_anova(self):
        data_frame = create_data_frame(self.csv_data)
        logging.info(f'Running two-way ANOVA on data: {data_frame[:1]}')

        # create a model
        model = ols('abundance ~ C(pan_colour) + C(canopy) + C(pan_colour):C(canopy)', data=data_frame).fit()
        self.two_way_anova_result = sm.stats.anova_lm(model, typ=2, alpha=self.alpha)

        logging.info(f'ANOVA results: {self.two_way_anova_result}')
        return self.two_way_anova_result, model.summary()


def create_data_frame(data_for_frame):
    data_frame = pd.DataFrame(data_for_frame)
    logging.info(f'Creating data frame: {data_frame[:1]}')
    return data_frame


path = 'data/invertebrate_data.csv'
data = CsvReader(path).read()
alpha_value = 0.05 # Set your desired alpha value here
anova = DataAnalysis(data, alpha=alpha_value)
result, summary = anova.two_way_anova()
print(result)
# print(summary)