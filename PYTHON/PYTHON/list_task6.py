guest_list : list[str] = ['haji', 'ali' , 'waheed']


print('Lets add more guestes')

guest_list.insert(0, 'shakeel')

guest_list.insert(2, 'yousaf')

guest_list.insert(5, 'shela')
print(guest_list)

for guest in guest_list:
    print(f"{guest.title()}! We are inviting you for the dinner ")