import	json

#parse json
mystring	=	'{"a":1,"b":2,"c":3,"d":4,"e":5}'
data	=	json.loads(mystring)
print	(data["a"])

#encode to json
str_json = json.dumps(data)
print (str_json)

