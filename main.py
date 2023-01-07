import json 
def ordenarValores():
	with open("db.json","r")as f:
		data = json.load(f)

	sorted_data = json.dumps(data, sort_keys = True)

	with open("db.json","w") as f:
		f.write(sorted_data)
