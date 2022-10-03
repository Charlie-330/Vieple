import json

input_stream = open("Test.json","r")
json_contents = input_stream.read().strip()
input_stream.close()
a_dict = json.loads(json_contents)


if 'Name' in a_dict:
     value = a_dict['Name']
     if value == 'Badges':
         print("Name =",value)
     else:
        print("error!")
        
if "CanRelist" in a_dict:
        if a_dict["CanRelist"]==True:
            print("CanRelist =",a_dict["CanRelist"])
        else:
            print("Error")
            
if "Promotions" in a_dict:
    promo_dict = a_dict["Promotions"]
    for i in promo_dict:
        if i['Name']=='Feature':
            print(i)
