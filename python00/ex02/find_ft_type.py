def all_thing_is_obj(object: any) -> int:
	dict_type = {
		list: "List :",
		tuple: "Tuple :",
		set: "Set :",
		dict: "Dict :",
		str: "{} is in the kitchen :"
	}

	obj_type = type(object)
	title = dict_type.get(obj_type, "Type not found")

	if title == "Type not found":
		print(title)
		return 42

	if obj_type is str:
		title = title.format(object)

	print(title, obj_type)
	return 42
