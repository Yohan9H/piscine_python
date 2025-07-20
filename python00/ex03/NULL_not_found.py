def NULL_not_found(object: any) -> int:
	dict_err = {
		type(None): "Nothing :",
		float: "Cheese :",
		int: "Zero :",
		str: "Empty :",
		bool: "Fake :"
	}

	err_type = type(object)
	title = dict_err.get(err_type, "Type not found")

	if title == "Type not Found":
		print(title)
		return 1
	
	if isinstance(object, str):
		if object == "":
			print("Empty :", type(object))
			return 0
		else:
			print("Type not Found")
			return 1

	print(title, object, err_type)
	return 0