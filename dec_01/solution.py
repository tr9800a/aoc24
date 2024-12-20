def read_columns_to_lists(filepath, delimiter="   "):
    list1 = []
    list2 = []

    with open(filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(delimiter)
            if len(parts) == 2:
                list1.append(int(parts[0]))
                list2.append(int(parts[1]))
    
    return list1, list2

column1, column2 = read_columns_to_lists("./lists.txt")

column1.sort()
column2.sort()

distance = 0

for i in range(len(column1)):
    x = abs(column1[i] - column2[i])
    distance += x
    
print(f"Total distance: {distance}")

def common_elements_lists(list1, list2):
    common1 = [x for x in list1 if x in list2]
    common2 = [x for x in list2 if x in list1]
    combined = common1 + common2
    
    return common1, common2

common1, common2 = common_elements_lists(column1, column2)

similarity = 0
for i in common1:
    c1 = common2.count(i)
    similarity += (c1 * i)

print(f"Similarity score: {similarity}")