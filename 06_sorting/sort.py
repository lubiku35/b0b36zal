def sortNumbers(data, condition):
    length = len(data)
 
    if condition == 'ASC':
        for i in range(length):
            for j in range(0, length - i - 1):
                if data[j] > data[j + 1]:
                    temp = data[j]
                    data[j] = data[j + 1]
                    data[j + 1] = temp
        return data
    elif condition == 'DESC':
        for i in range(length):
            for j in range(0, length - i - 1):
                if data[j] < data[j + 1]:
                    temp = data[j]
                    data[j] = data[j + 1]
                    data[j + 1] = temp
        return data
    else:
        raise ValueError('Invalid input data')
 
def sortData(weights, data, condition):
    length_weights = len(weights)
    length_data = len(data)
 
    if length_data != length_weights:
        raise ValueError('Invalid input data')
 
    assignments = list(zip(weights, data))
     
    if condition == 'ASC':
        item_iterator = 0
        for i in range(len(assignments) - 1):
            for j in range(len(assignments) - 1):
                if assignments[j][item_iterator] > assignments[j + 1][item_iterator]:
                    temp = assignments[j]
                    assignments[j] = assignments[j + 1]
                    assignments[j + 1] = temp
        output = []
        for i in range(len(assignments)):
            output.append(assignments[i][1])
        return output
    elif condition == 'DESC':
        item_iterator = 0
        for i in range(len(assignments) - 1):
            for j in range(len(assignments) - 1):
                if assignments[j][item_iterator] < assignments[j + 1][item_iterator]:
                    temp = assignments[j]
                    assignments[j] = assignments[j + 1]
                    assignments[j + 1] = temp
        output = []
        for i in range(len(assignments)):
            output.append(assignments[i][1])
        return output
    else:
        raise ValueError('Invalid input data')