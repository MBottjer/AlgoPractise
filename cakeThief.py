def max_duffel_bag_value(cake_tuples, capacity):

	cake_with_best_ratio = (1,1)

	for attributes in cake_tuples:
		if attributes[1]/attributes[0] > cake_with_best_ratio[1]/cake_with_best_ratio[0]:
			cake_with_best_ratio = (attributes[0],attributes[1])


cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20
max_duffel_bag_value(cake_tuples, capacity)