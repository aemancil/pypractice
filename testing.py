#index operater[] = gives acccess to a sequence's element
name = "elaine"
#if(name[0].islower):
#    name = name.capitalize()
first_name = name[:3].upper()
last_name = name[3:].lower()
last_ch = name[-1]#last element will be -1
print(first_name)
print(last_name)
print(last_ch)