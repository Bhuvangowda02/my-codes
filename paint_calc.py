import math
height=int(input('enter the height:'))
width=int(input('enter the width:'))
coverage=5

def paint_calculator(height,width,coverage):
    cans=(height*width)/coverage
    round_off=math.ceil(cans)
    print(f"you'll need {round_off} cans to paint the wall")
    
paint_calculator(height,width,coverage)
