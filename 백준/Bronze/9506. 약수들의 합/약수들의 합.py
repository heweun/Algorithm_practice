a = sorted(list(map(int,open(0).read().split())))

def yaksu(num):
    yaksu_list = []
    for n in range(1,num+1):
        if num%n == 0:
            yaksu_list.append(n)

    return yaksu_list

for i in a:
    if sum(yaksu(i)[:-1]) == i:
        print(yaksu(i)[-1],'='," + ".join(map(str,yaksu(i)[:-1])))
    elif i == -1:
        pass
    else:
        print(yaksu(i)[-1],"is NOT perfect.")