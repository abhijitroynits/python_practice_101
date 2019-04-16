# It's also important to create functions that process data , and
# return values which can later be used in other parts of our programs.


def allowed_dating_age(your_age):
    girls_age = (your_age // 2) + 7
    return girls_age


for age in range(20, 60, 5):
    dating_age_limit = str(allowed_dating_age(age))
    age = str(age)
    print("At age " + age + ", you can date girls with age >= "
          + dating_age_limit + " yrs.")


