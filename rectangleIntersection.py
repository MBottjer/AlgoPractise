def determineIntersection(rectangle_one, rectangle_two):

	intersecting_rectangle = {}

	x_and_width = find_range_overlap(rectangle_one['x'], rectangle_one['width'], rectangle_two['x'], rectangle_two['width'])
	y_and_height = find_range_overlap(rectangle_one['y'], rectangle_one['height'], rectangle_two['y'], rectangle_two['height'])

	intersecting_rectangle['x'], intersecting_rectangle['width'] = x_and_width[0], x_and_width[1]
	intersecting_rectangle['y'], intersecting_rectangle['height'] = y_and_height[0], y_and_height[1]

	print intersecting_rectangle

def find_range_overlap(point1, length1, point2, length2):

	start_point = max(point1, point2)
	end_point = min(point1+length1, point2+length2)

	if(start_point >= end_point):
		print "don't intersect"



	overlap_length = end_point - start_point

	return (start_point, overlap_length)

rectangle1 = {'x':0, 'y':0, 'height':6, 'width':8}
rectangle2 = {'x':4, 'y':5, 'height':4, 'width':4}

determineIntersection(rectangle1, rectangle2)

rectangle3 = {'x':0, 'y':0, 'height':3, 'width':4}
rectangle4 = {'x':1, 'y':1, 'height':2, 'width':2}

determineIntersection(rectangle3, rectangle4)



