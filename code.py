import random 
import plotly_express as px
import plotly.figure_factory as ff

count=[]
dice_result=[]  
for numbers in range(0,20):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(numbers)

fig=ff.create_distplot([dice_result],['result'])
fig.show()    



