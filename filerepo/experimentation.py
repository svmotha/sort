'''
NB: Not part of the code, just used to model sorting as practice

Test module for sorting an item just once in a list even if it
occurs more than once. This will help with:
    Making sure we know which artist name occursmore than once
    in the list of artists.
'''
l = [1, 2, 3, 4, 5, 6, 1, 6, 1, 2]
lis_o = []

for i in range(len(l)):
    a = [x for x, val in enumerate(l) if val == l[i]]
    if len(a) > 1:
        if l[i] in lis_o:
            pass
        else:
            lis_o.append(l[i])

    elif len(a) == 1:
        lis_o.append(l[i])
