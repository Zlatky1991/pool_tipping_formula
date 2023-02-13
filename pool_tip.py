question = input("How many servers: ")
server = int(question) #how many servers
points_amount = 0
tip_amount = 0 
average = 0
pool_tip = 0
list_server_points = []

for _ in range(1, server + 1):
    question_two = input("Server tip amount: ")
    tip = int(question_two)
    question_three = input("How many points for this server: ")
    server_points = int(question_three)
    list_server_points.append(server_points)

    tip_amount += tip
    points_amount += server_points

    average = tip_amount / points_amount

point_one, point_two, point_three, point_four, point_five,\
point_six, point_seven, point_eight, point_nine = 0, 0, 0, \
                                                  0, 0, 0, 0, 0, 0
print(f"The total points are {points_amount}.")
print(f"The total pool tip amount is {tip_amount}$.")

for i in list_server_points:
    if i == 1:
        pool_tip = average * i
        point_one += 1
        if point_one > 1:
            continue
        else:
            print(f'The server with 1 points has: {pool_tip:.2f}$ pool tip.')
    elif i == 2:
        pool_tip = average * i
        point_two += 1
        if point_two > 1:
            continue
        else:
            print(f'The server with 2 points has: {pool_tip:.2f}$ pool tip.')
    elif i == 3:
        pool_tip = average * i
        point_three += 1
        if point_three > 1:
            continue
        else:
            print(f'The server with 3 points has: {pool_tip:.2f}$ pool tip.')
    elif i == 4:
        pool_tip = average * i
        point_four += 1
        if point_four > 1:
            continue
        else:
            print(f'The server with 4 points has: {pool_tip:.2f}$ pool tip.')
    elif i == 5:
        pool_tip = average * i
        point_five += 1
        if point_five > 1:
            continue
        else:
            print(f'The server with 5 points has: {pool_tip:.2f}$ pool tip.')
    elif i == 6:
        pool_tip = average * i
        point_six += 1
        if point_six > 1:
            continue
        else:
            print(f'The server with 6 points has: {pool_tip:.2f}$ pool tip.')
    elif i == 7:
        pool_tip = average * i
        point_seven += 1
        if point_seven > 1:
            continue
        else:
            print(f'The server with 7 points has: {pool_tip:.2f}$ pool tip.')
    elif i == 8:
        pool_tip = average * i
        point_eight += 1
        if point_eight > 1:
            continue
        else:
            print(f'The server with 8 points has: {pool_tip:.2f}$ pool tip.')
    elif i == 9:
        pool_tip = average * i
        point_nine += 1
        if point_nine > 1:
            continue
        else:
            print(f'The server with 9 points has: {pool_tip:.2f}$ pool tip.')



