def chase(a1_speed, t2_speed, advantage):
    return advantage + t2_speed * advantage / (a1_speed - t2_speed)

        
print(chase(6, 3, 2))
"""

"""               



