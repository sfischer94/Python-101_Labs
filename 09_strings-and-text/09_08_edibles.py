# Extract four words of edible food items from the sentence below.
# Use only string slicing to pick them out!
# Feel free to use pen and paper to number the indices
# and find the locations quicker.
#
# What dish can you make from these ingredients? :)

s = "They grappled with their leggins before going to see the buttercups flourish."
#print(s.index("buttercups"))
#print(len("buttercups"))
print(s[57:67]) #buttercups

#print(s.find("flour"))
#print(len("flour"))
print(s[68:73]) #flour

print(s[5:9] + s[11:12]) #grape

#print(s.index("leg"))
print(s[25:28]) #leg