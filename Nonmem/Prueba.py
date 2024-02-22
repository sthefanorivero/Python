from pharmpy.modeling import read_model
model = read_model("C:/CTI/Neurax Buprenorphine/NM_PK_Buprenorphine_alldoses/Buprenorphine.SD.alldoses.PK.2cp.weibull.TRT2.lst")
print(model)

print(model.name)

parset = model.parameters
print(parset)
print(parset.inits)
rvs = model.random_variables
print(rvs)

statements = model.statements
print(statements)

ests = model.estimation_steps
print(ests)

from pharmpy.tools import read_modelfit_results
results = read_modelfit_results('C:/CTI/Neurax Buprenorphine/NM_PK_Buprenorphine_alldoses/Buprenorphine.SD.alldoses.PK.2cp.weibull.TRT2.out')
print(results)
print(results.ofv)
print(results.parameter_estimates)
print(results.standard_errors)
print(results.relative_standard_errors)
#print(results.covariance_matrix)
#print(results.correlation_matrix)
#print(results.individual_ofv)
#print(results.predictions) para tener las predicciones PRED IPRED de cada sujeto.
results.residuals #RES Y CWRES
results.individual_estimates #estimadores individuales (EBEs)
from pharmpy.modeling import *
print_model_code(model)
get=get_observations(model)
print(get)
print(get_number_of_observations(model))

