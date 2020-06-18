from msvcrt import getch; import sys
ques=input('Ask any question and I will answer! ')
print(ques)
pt='peter, please predict the answer                '
ans=''
count=1
print('Enter Petition: ')
key=getch()
if key==b'.':
    print(pt[0],end='')
    sys.stdout.flush()
    while True:
        key = getch()
        if key!=b'.':
            ans = ans + key.decode()
            print(pt[count], end='')
            sys.stdout.flush()
            count+=1
        if key == b'\r':
            break
else:
    print(pt[0],end="")
    while True:
        key = getch()
        if key != b'.':
            print(pt[count],end="");sys.stdout.flush()
        elif key == b'.':
            print(pt[count],end="");sys.stdout.flush()
            while True:
                key = getch()
                if key != b'.':
                    answer += key
                    print(pt[count], end="") ;sys.stdout.flush()
                elif key == b'.':
                    print(pt[count], end="");sys.stdout.flush()
                    count += 1
                    for i in range(count, 42):
                        key = getch()
                        print(key.decode(), end="");sys.stdout.flush()
                        count += 1
                    break
                count += 1
            break
        count += 1

print("\npeter says,",ans)