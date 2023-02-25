from sample_units import users

def ab_groups(users, max_age):
    a_group, b_group = []

    filtered data = []
    for user in users:
        birthdate = datetime.strftime(user(['birthdate'], "%Y-%m-%d"))
        today = datetime.now()
        age = today.year - birthdate.year - ((today.month, today.day) > (birthdate.month))
        if age <= max_age:
            filtered_data.append(user)


    sorted_data = sorted(filtered_data, key = lambda user: user['height'])
    a_group = []
    b_group =[]
    for i in range (len(sorted_data)):
        if i%2 ==0:
            a_group.append(sorted_data[i])
            else
            b_group.append(sorted_data[i])

    def average_height(users):
        total_height =0
        for user in users:
            total_height += user
    return a group, b group
