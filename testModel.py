from model.model import Model

model = Model()
print(model.build_weighted_graph(2000))

print(model.get_edges_weight_min_max())

print(model.count_edges_by_threshold(4))

print(model.cammino_minimo(4))