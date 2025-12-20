import scipy.stats as stats
import numpy as np

def HotellingsT2Test(X, Y):
    '''Realiza la prueba T2 de Hotelling para dos muestras

       Parámetros
       ----------
       X: pd.DataFrame
           Matriz de datos de la primera población
       Y: pd.DataFrame
           Matriz de datos de la segunda población

       Output
       ------
       statistic: float
           Valor de la estadística de prueba
       p-value: float
           P-value resultante
    '''

    ## Encontramos los tamaños de
    ## muestra y el número de variables
    n, p = X.shape
    m = Y.shape[0]

    ## Calculamos la diferencia de medias
    ## muestrales, las matrices de covarianza
    ## y la matriz de covarianza agrupada
    delta = (X.mean(axis = 0) - Y.mean(axis=0)).values
    Sx = X.cov()
    Sy = Y.cov()
    S_pooled = ((n-1)*Sx+(m-1)*Sy)/(n+m-2)

    ## Calculamos la estadística de prueba
    t2 = (n*m)/(n+m)*(delta@np.linalg.inv(S_pooled)@delta)
    statistic = (n+m-p-1)/(p*(n+m-2))*t2

    ## Calculamos el p-value
    p_value = 1 - stats.f.cdf(statistic, p,(n+m-p-1))

    ## Imprimimos el resultado
    print(f"Estadística de prueba: {statistic}\nGrados de libertad: {p}, {n + m - p - 1}\np-value: {p_value}")

    return statistic, p_value