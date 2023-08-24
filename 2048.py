# 2048 GAME
import random
A = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
list = [0,1,2,3]
A[random.choice(list)][random.choice(list)]=2

def u_choice(A,u_input):
    if u_input == 'w':
        i=0
        for j in range(0,4):
            if A[i][j]!=0 or A[i+1][j]!=0 or A[i+2][j]!=0 or A[i+3][j]!=0:
                if A[i][j]==0:
                    while A[i][j]==0:
                        A[i][j]=A[i+1][j]
                        A[i+1][j]=A[i+2][j]
                        A[i+2][j]=A[i+3][j]
                        A[i+3][j]=0
                elif A[i+1][j]==0 and (A[i+2][j]!=0 or A[i+3][j]!=0):
                    while A[i+1][j]==0:
                        A[i+1][j]=A[i+2][j]
                        A[i+2][j]=A[i+3][j]
                        A[i+3][j]=0
                elif A[i+2][j]==0 and A[i+3][j]!=0:
                    while A[i+2][j]==0:
                        A[i+2][j]=A[i+3][j]
                        A[i+3][j]=0
        i=0
        for j in range(0,4):
            if A[i][j]==A[i+1][j]:
                A[i][j]=A[i][j]+A[i+1][j]
                A[i+1][j]=A[i+2][j]
                A[i+2][j]=A[i+3][j]
                A[i+3][j]=0
            elif A[i+1][j]==A[i+2][j]:
                A[i+1][j]=A[i+1][j]+A[i+2][j]
                A[i+2][j]=A[i+3][j]
                A[i+3][j]=0
            elif A[i+2][j]==A[i+3][j]:
                A[i+2][j]=A[i+2][j]+A[i+3][j]
                A[i+3][j]=0

    elif u_input == 's':
        i=0
        for j in range(0,4):
            if A[i][j]!=0 or A[i+1][j]!=0 or A[i+2][j]!=0 or A[i+3][j]!=0:
                if A[i+3][j]==0:
                    while A[i+3][j]==0:
                        A[i+3][j]=A[i+2][j]
                        A[i+2][j]=A[i+1][j]
                        A[i+1][j]=A[i][j]
                        A[i][j]=0
                elif A[i+2][j]==0 and (A[i+1][j]!=0 or A[i][j]!=0):
                    while A[i+2][j]==0:
                        A[i+2][j]=A[i+1][j]
                        A[i+1][j]=A[i][j]
                        A[i][j]=0
                elif A[i+1][j]==0 and A[i][j]!=0:
                    while A[i+1][j]==0:
                        A[i+1][j]=A[i][j]
                        A[i][j]=0
        i=0
        for j in range(0,4):
            if A[i+3][j]==A[i+2][j]:
                A[i+3][j]=A[i+3][j]+A[i+2][j]
                A[i+2][j]=A[i+1][j]
                A[i+1][j]=A[i][j]
                A[i][j]=0
            elif A[i+2][j]==A[i+1][j]:
                A[i+2][j]=A[i+2][j]+A[i+1][j]
                A[i+1][j]=A[i][j]
                A[i][j]=0
            elif A[i+1][j]==A[i][j]:
                A[i+1][j]=A[i+1][j]+A[i][j]
                A[i][j]=0

    elif u_input == 'a':
        j=0
        for i in range(0,4):
            if A[i][j]!=0 or A[i][j+1]!=0 or A[i][j+2]!=0 or A[i][j+3]!=0:
                if A[i][j]==0:
                    while A[i][j]==0:
                        A[i][j]=A[i][j+1]
                        A[i][j+1]=A[i][j+2]
                        A[i][j+2]=A[i][j+3]
                        A[i][j+3]=0
                elif A[i][j+1]==0 and (A[i][j+2]!=0 or A[i][j+3]!=0):
                    while A[i][j+1]==0:
                        A[i][j+1]=A[i][j+2]
                        A[i][j+2]=A[i][j+3]
                        A[i][j+3]=0
                elif A[i][j+2]==0 and A[i][j+3]!=0:
                    while A[i][j+2]==0:
                        A[i][j+2]=A[i][j+3]
                        A[i][j+3]=0
        j=0
        for i in range(0,4):
            if A[i][j]==A[i][j+1]:
                A[i][j]=A[i][j]+A[i][j+1]
                A[i][j+1]=A[i][j+2]
                A[i][j+2]=A[i][j+3]
                A[i][j+3]=0
            elif A[i][j+1]==A[i][j+2]:
                A[i][j+1]=A[i][j+1]+A[i][j+2]
                A[i][j+2]=A[i][j+3]
                A[i][j+3]=0
            elif A[i][j+2]==A[i][j+3]:
                A[i][j+2]=A[i][j+2]+A[i][j+3]
                A[i][j+3]=0

    elif u_input == 'd':
        j=0
        for i in range(0,4):