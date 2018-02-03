udata = []
sorted_data = []
for x in range(1, 37):
	for y in range(1, 37):
		for z in range(1, 37):
			if x * y * z == 36:
				data.append([x, y, z])
for triplet in data:
	min_num = min(triplet)
	max_num = max(triplet)
	del triplet[triplet.index(min_num)]
	del triplet[triplet.index(max_num)]
	middle = triplet[0]
	triplet = (min_num, middle, max_num)
	if triplet not in sorted_data:
		sorted_data.append(triplet)

sum_dict = {}
for triplet in sorted_data:
	sum_val = sum(triplet)
	array_of_vals = sum_dict.get(sum_val, [])
	array_of_vals.append(triplet)
	sum_dict[sum_val] = array_of_vals

for sumID in sum_dict:
	if len(sum_dict[sumID]) > 1:
		oldest =[]
		for posibility in sum_dict[sumID]:
			oldest.append(max(posibility))
		youngest_oldest = min(oldest)
		print(sum_dict[sumID][oldest.index(youngest_oldest)])
				
