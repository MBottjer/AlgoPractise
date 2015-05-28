def find_missing_drone(list_of_drones):

	id_map = {}

	for drone_id in list_of_drones:
		if drone_id not in id_map:
			id_map[drone_id] = 1
		else:
			id_map[drone_id] += 1

	for drone_id in id_map:
		if id_map[drone_id] == 1:
			print False
			return

	print True

find_missing_drone([2,2,2,1,2,2,2])

def find_undelivered_packages(list_of_drones):

	unique_delivery_id = 0

	for delivery_id in list_of_drones:

		unique_delivery_id ^= delivery_id

	return unique_delivery_id