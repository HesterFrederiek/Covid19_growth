"""
sources:    Formulas:
            https://royalsociety.org/-/media/policy/projects/set-c/set-covid-19-R-estimates.pdf
            Estimate of generation time T:
            https://twitter.com/C_Althaus/status/1327572765784858625
            https://twitter.com/C_Althaus/status/1327567433142558725/photo/1
"""


import numpy as np
import pandas as pd



# growth rate r=(R-1)/T,  generation time T, abgeschätzt auf 4.8 (tweets Althaus)
def growth_rate(R, T=4.8):
    return (R-1)/T


def add_growth_rate(df, T=4.8):
    df['Mittlere growth rate'] = growth_rate(df['Mittlere effektive Reproduktionszahl'], T)
    df['Obere Grenze growth rate'] = growth_rate(df['Obere Grenze der effektiven Reproduktionszahl'], T)
    df['Untere Grenze growth rate'] = growth_rate(df['Untere Grenze der effektiven Reproduktionszahl'], T)
    return df


# verdopplung macht sinn wenn R>1 (equivalent: r>0), sonst verdoppelung=None
def verdoppelung(r):
    return np.where(r > 0, np.log(2)/r, None)


def add_verdoppelung(df, T=4.8):
    df = add_growth_rate(df, T)
    df['Mittlere Verdoppelung'] = verdoppelung(df['Mittlere growth rate'])
    df['Obere Grenze Verdoppelung'] = verdoppelung(df['Obere Grenze growth rate'])
    df['Untere Grenze Verdoppelung'] = verdoppelung(df['Untere Grenze growth rate'])
    return df


def return_data(filename, df, T=4.8):
    df = add_verdoppelung(df, T)
    df.to_csv(filename)


def append_file(old_filename, new_filename, T=4.8):
    df = pd.read_csv(old_filename, sep=';')
    return_data(new_filename, df, T)


def filter_basel(df):
    return df[df['Region'] == 'BS']


def open_csv_file(path):
    '''
    turn csv file at path into dataframe
    '''
    with open(path, 'r') as f:
        return pd.read_csv(f, sep=';')


if __name__ == '__main__':
   path = 'data.csv'
   path_newfile = 'verdoppelung.csv'
   append_file(path, path_newfile, T=4.8)


