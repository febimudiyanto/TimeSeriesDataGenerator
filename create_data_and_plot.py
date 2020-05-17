import pandas as pd
from matplotlib import pyplot
from generate_evc_time_data import TimeValueGenerator

def main(i):

    # Class instance
    time_generator = TimeValueGenerator(50, 5, 30, 'data/generate_data_'+str(i)+'.csv')

    # Calls the generate method
    time_generator.generate_time_values()

    df = pd.read_csv('data/generate_data_'+str(i)+'.csv')
    df.groupby('date_time').cumsum()['power'].plot(x='date_time', y='power')
    pyplot.show()


if __name__ == '__main__':
    for i in range(1,5):
        main(i)
