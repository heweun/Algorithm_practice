def solution(wallpaper):
    min_list = []
    max_list = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                min_list.append((i,j))
                max_list.append((i+1,j+1))
                
    answer = [min(list(map(lambda x:x[0], min_list))),
              min(list(map(lambda x:x[1], min_list))),
              max(list(map(lambda x:x[0], max_list))),
              max(list(map(lambda x:x[1], max_list)))]

    return answer