def print_models(unprintedDesigns, completedModels):
	'''Simulate printing each design, until none are left.
	Move each design to completed_models after printing.'''
	while unprintedDesigns:
		current_design = unprintedDesigns.pop()
		# Simulate creating a 3D print from the design.
		print("Printing model: " + current_design)
		completedModels.append(current_design)


def show_completed_models(completedModels):
	'''Show all the models that were printed.'''
	print("\nThe following models have been printed:")
	for completedModel in completedModels:
		print(completedModel)

