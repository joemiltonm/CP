

def soft_drink():
    q = list(map(int, input().split()))
    friends = q[0]
    bottles = q[1]
    ml = q[2]
    limes = q[3]
    lime_slices = q[4]
    salt = q[5]
    toast_per_friend = q[6]
    salt_per_toast = q[7]

    total_drink = bottles * ml
    total_slices = limes * lime_slices
    total_salt = salt

    values = []
    toast_drink = total_drink // (toast_per_friend * friends)
    toast_slices = total_slices // friends
    toast_salt = total_salt // (salt_per_toast * friends)

    values.append(toast_drink)
    values.append(toast_slices)
    values.append(toast_salt)

    return min(values)


print(soft_drink())





