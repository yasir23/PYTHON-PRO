guest_list : list[str] = ['haji', 'ali' , 'waheed']

isNotcomming = guest_list.pop(0)

print(f"In the dinner {isNotcomming} can't make it! ")

guest_list.append('muhammad')

for guest in guest_list:
    print(f"We invite to the dinner {guest.upper()}")



