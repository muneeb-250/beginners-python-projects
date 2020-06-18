_list1_=[]
_len_numbers=int(input('How many numbers you want to input in list '))
for i in range(_len_numbers):
    num=int(input('Enter numbers '))
    _list1_.append(num)

_list1_=tuple(_list1_)
mini = _list1_[0]
maxi = _list1_[0]
for i in range(_len_numbers):
    if _list1_[i] > maxi:
        maxi = _list1_[i]
    elif _list1_[i] < mini:
        mini = _list1_[i]
print("minimum is", mini ,"\nmaximum is", maxi)
