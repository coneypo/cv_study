##############
t1 = (325, 158)
t2 = (427, 174)
t3 = (286, 241)
t4 = (398, 266)

t_list = [t1,t2,t3,t4]

print(t_list)
t_list= sorted(t_list, key=lambda t: t[0])

print(t_list)
for i in range(len(t_list)):
    print(t_list[i][0])