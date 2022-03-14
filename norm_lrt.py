import pandas as pd
import rpy2.robjects as robjects
from rpy2.robjects.vectors import FloatVector
import numpy as np
from pathlib import Path

CWD = Path(__file__).parents[0]

# Print iterations progress
def printProgressBar(iteration, total, prefix = '', suffix = '', decimals = 1,
                     length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

# Defining the R script and loading the instance in Python
r = robjects.r
r['source'](CWD /'NormLRT.R')
lrt_test_func_r = robjects.globalenv['LRT_test']    
lrt_validation_func_r = robjects.globalenv['LRT_validator']
sink_func_r = r.objects.globalenv['sink']

def lrt_test(df: pd.DataFrame, label: str) -> pd.DataFrame:
    sink_func_r(CWD/'r_log_sink.txt')
    lrt_stats = {}
    # Reading and processing data in R

    cols = len(df.columns)
    for i,c in enumerate(df.columns):
        vec = df[c].values
        vec = FloatVector(vec)
        #Invoking the R function and getting the result
        result = lrt_test_func_r(vec)
        #Converting it back to a pandas dataframe.
        lrt_stats[c.split(' ')[0]] = result
        printProgressBar(iteration=i, total=cols, prefix=f'{label} Skew_LRT: '+c)
    lrt_stats = {k:np.asarray(v) for k,v in lrt_stats.items()}

    new_df = pd.DataFrame.from_dict(lrt_stats, columns=['Skew_LRT'], orient='index')
    
    return new_df