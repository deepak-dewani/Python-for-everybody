fname = input("enter file name: ")
if len(fname) < 1: fname = "open.txt.txt"
hand = open(fname) 

# for lin in hand:
#     lin = lin.rstrip()
#     # print(lin)
#     wds = lin.split()
#     print(wds)