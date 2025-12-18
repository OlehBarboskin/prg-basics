phone = {
    "OS": "Android",
      "Brand": "Samsung",
      "Model": "Galaxy S21"
}

for key, value in phone.items():
    print(f"{key}: {value}")
print(type({"landline":"12332323"}))

for thing in phone:
      print(thing)

for count in phone.values():
      print(count)

if 'OS' in phone:
     
      print("Key 'OS' found in phone dictionary.")