list_1 = [4, 9, 8, 7, 5, 2, 13]

new_list = sorted(list_1, reverse=True)

l = len(new_list)

sub = new_list[0] - new_list[l-1]

print(sub)