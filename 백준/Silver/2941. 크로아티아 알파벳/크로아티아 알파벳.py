cr_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()

for i in cr_list:
  if i in word:
    word = word.replace(i,"A")
print(len(word))