# Suppose we create a social network, and
# we set a default value for the gender field


def get_gender(sex='Unknown'):
    try:
        if sex.lower() != 'unknown':
            if sex.lower() == 'm':
                return 'Male'
            elif sex.lower() == 'f':
                return 'Female'
    except Exception as e:
        print('Invalid Input , Flag:', e)

    return 'Unknown'


print("Sex of user who entered 'M' = " + get_gender('M'))
print("Sex of user who entered 'F' = " + get_gender('F'))
print("Sex of user who entered '' = " + get_gender())
print("Sex of user who entered '!FunkY'= " + get_gender('!FunkY'))
print("Sex of user who entered 'None'= " + get_gender(None))

