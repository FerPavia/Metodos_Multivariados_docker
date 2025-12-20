import scipy.stats as stats
import numpy as np
import pandas as pd

def bonferroni(X, alpha = 0.05):
    '''Calcula intervalos de confianza simultáneos con corrección de Bonferroni

       Parámetros
       ----------
       X: pd.DataFrame
           Matriz de datos
       alpha: float
           Nivel de significancia

       Output
       ------
       res: pd.DataFrame
           Data frame con los nombres de las variables, sus medias muestrales y los límites inferior y superior del intervalo de confianza con corrección de Bonferroni
    '''
    ## Encontramos el tamaño de
    ## muestra y número de variables
    n, p = X.shape

    ## Extraemos los nombres de las variables
    cols = X.columns

    ## Calculamos las medias
    ## muestrales y las varianzas
    ## muestrales de cada variable
    mm = X.mean(axis=0)
    ss = X.var(axis = 0)

    ## Encontramos el cuantil
    ## de la distribución t
    tt = stats.t.ppf(1-alpha/(2*p),n-1)

    ## Encontramos los límites
    ## inferior y superior del
    ## intervalo corregido
    lower = mm - tt * np.sqrt(ss/n)
    upper = mm + tt * np.sqrt(ss/n)

    ## Juntamos los resultados
    ## en un solo data frame
    res = pd.DataFrame({"variable": cols,
                        "mean": mm,
                        "lower": lower,
                        "upper": upper})

    return res