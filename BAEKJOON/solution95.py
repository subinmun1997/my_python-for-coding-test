num = int(input())

draw = num * 2 - 1

for i in range(draw):

    if(i <= num-1): # first ~ middle
        print(" "*i + "*"*(draw-2*i))
    else:   # middle+1 ~ last
        print(" "*(draw-i-1) + "*"*(2*(i+1)-draw))