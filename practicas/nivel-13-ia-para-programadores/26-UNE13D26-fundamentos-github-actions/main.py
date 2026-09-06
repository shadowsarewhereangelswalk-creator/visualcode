jobs={"test":{"runner":"ubuntu-latest","steps":["checkout","setup-python","tests"]},"deploy":{"runner":"ubuntu-latest","steps":["checkout","deploy"]}}
for nombre,config in jobs.items(): print(nombre,config)
