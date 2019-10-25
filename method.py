import json
import operator

with open('input.txt') as f:
	json_data = json.loads(f.read())

with open('alfa.txt') as f:
	alfa = json.loads(f.read())

def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True


def add(json_data, alfa):
	F = {}
	for U in json_data.keys():
		sum = 0
		for k in json_data[U].keys():
			sum += json_data[U][k]*alfa[k]
		F[U] = sum
		sum = 0
	return F


def mult(json_data, alfa):
	F = {}
	for U in json_data.keys():
		prod = 1
		for k in json_data[U].keys():
			prod *= json_data[U][k]
		F[U] = prod
		prod = 1
	return F


def min(json_data, alfa):
	F = {}
	for U in json_data.keys():
		i_min = list(alfa.keys())[0]
		min = json_data[U][i_min]/alfa[i_min]
		for k in json_data[U].keys():
			F_k = json_data[U][k]/alfa[k]
			if F_k < min:
				min = F_k
		F[U] = min 
	return F


def max(json_data, alfa):
	F = {}
	for U in json_data.keys():
		i_min = list(alfa.keys())[0]
		max = json_data[U][i_min]*alfa[i_min]
		for k in json_data[U].keys():
			F_k = json_data[U][k]*alfa[k]
			if F_k > max:
				max = F_k
		F[U] = max
	return F


with open('output_max.txt', 'w') as f:
	f.write(str(max(json_data, alfa)))





