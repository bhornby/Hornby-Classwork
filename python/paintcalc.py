# to calculate the amount of paint needed to paint a room
# assume 1L of paint covers 11sqM


# rs = room size
rs = input("how large is the room minus all unpaintable surfaces? (in sq m)")

lp = (int(rs)//11 )
# lp = litres of paint



print("your room is " + rs + " sq m")


print("you need ",lp," litres of paint")