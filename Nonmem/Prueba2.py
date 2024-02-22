from pharmpy.modeling import load_example_model
from pharmpy.tools import fit

model = load_example_model('pheno')
results = fit(model)
print(results)