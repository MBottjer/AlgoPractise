# first attempt

class TempTracker:

	def __init__(self):
		self.temperatures = []

	def insert(self, temperature):
		self.temperatures.append(temperature)

	def get_max(self):
		sorted(self.temperatures)[-1]

	def get_min(self):
		sorted(self.temperatures)[0]

	def get_mean(self):
		current_total, average = 0, 0
		number_of_values = len(self.temperatures)-1
		for number in self.temperatures:
			current_total += number
		average = float(current_total) / number_of_values
		print average

	def get_mode(self):
		current_index = 0
		count = 1

		for i in range(len(self.temperatures)):
			if(count == 0):
				current_index = i
				count = 1
			elif(self.temperatures[i] == current_index):
				count += 1
			else:
				count -= 1
		print self.temperatures[current_index]

temp_tracker = TempTracker()
temp_tracker.insert(1)
temp_tracker.insert(2)
temp_tracker.insert(5)
temp_tracker.insert(3)
temp_tracker.insert(1)
temp_tracker.insert(1)

print temp_tracker.get_mode()

# second attempt

class SecondTempTracker():

	def __init__(self):
		self.max = None
		self.min = None

		self.mean = None
		self.total_sum = 0.0
		self.total_numbers = 0

		self.mode = None
		self.occurences = [0]*111
		self.max_occurences = 0

	def insert(self, temperature):
		if not self.max or temperature > self.max:
			self.max = temperature
		if not self.min or temperature < self.min:
			self.min = temperature
		self.total_numbers += 1
		self.total_sum += temperature
		self.mean = self.total_sum / self.total_numbers

		self.occurences[temperature] += 1
		if self.occurences[temperature] > self.max_occurences:
			self.mode = temperature
			self.max_occurences = self.occurences[temperature]

	def get_max(self):
		print self.max

	def get_min(self):
		print self.min

	def get_mean(self):
		print self.mean

	def get_mode(self):
		print self.mode

	def get_mean(self):
		print self.mode

temp_tracker_two = SecondTempTracker()
temp_tracker_two.insert(1)
temp_tracker_two.insert(2)
temp_tracker_two.insert(5)
temp_tracker_two.insert(3)
temp_tracker_two.insert(1)
temp_tracker_two.insert(1)

print temp_tracker_two.get_mode()
