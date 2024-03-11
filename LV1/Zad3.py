def Average(lst):
    return sum(lst) / len(lst)

lstEmpty=[]
while True:
    x=input()
    if x=="Done":
        break
    elif x.isnumeric() == False:
        print("Upisite broj")
    else:
        lstEmpty.append(int(x))

print(len(lstEmpty),"brojeva")
print("Prosjek: ",Average(lstEmpty))
print("Minimalni clan: ",min(lstEmpty))
print("Maksimalni clan: ",max(lstEmpty))
lstEmpty.sort()
print(lstEmpty)
