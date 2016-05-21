#Sandwiches

def topping_list(*items):
    print("\nSummarize list of topping you order")
    for item in items:
        print("- " + item)

topping_list('cheeses', 'tomato', 'onino')

#User Profile

def build_profile(first_name, last_name, **others):
    info = {}
    info['name'] = first_name
    info['lastname'] = last_name
    for key, value in others.items():
        info[key] = value
    return info

info = build_profile('Big', 'Biggy', girlfriend='none', money='no money')
print(info)


