import pymc3 as pm 

# El problema de la moneda
# de 100 lanzamientos 80 caras
n = 100
caras = 80

# Creación del modelo
niter = 2000
with pm.Model() as modelo_moneda:
    # a priori
    p = pm.Beta('p', alpha=2, beta=2)
    # likelihood
    y = pm.Binomial('y', n=n, p=p, observed=caras)