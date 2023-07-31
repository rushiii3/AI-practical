moveTower(height,fromPole,toPole,withPole):
    if height>=1:
        moveTower(height-1,toPole,fromPole,withPole)
