my_dict = {
    "name": "Tanveer Chawla",
    "roll_number": 1024160035,
    "branch": "CSE",
    "age": 20,
    "city": "Patiala",
}

print(my_dict)

my_dict["location"] = my_dict.pop("city")
print(my_dict)

my_dict["cgpa"] = 8.73
print(my_dict)

my_dict["age"] +=1
print(my_dict)

dict_pop = my_dict.copy()
removed_branch = dict_pop.pop("branch")
print("Removed branch:", removed_branch)
print("Dictionary after popping branch:", dict_pop)

dict_del = my_dict.copy()
del dict_del["branch"]
print("Dictionary after deleting branch:", dict_del)

##pop returns the removed value but del just delete it without returning

for key, value in my_dict.items():
    print(key, "→", value)

if "email" in my_dict:
    print("Email:", my_dict["email"])
else:
    print("Email key does not exist.")


friend_dict = {
    "name": "Sheru",
    "roll_no": "1024160044",
    "branch": "CSE",
    "age": 20,
    "city": "Chandigarh"
}

merged_dict = {**my_dict, **friend_dict}
print("Merged Dictionary:", merged_dict)

string_values = {
    key: value
    for key, value in my_dict.items()
    if isinstance(value, str)
}
print(string_values)