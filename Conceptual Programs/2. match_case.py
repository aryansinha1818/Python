
def categorize_number(num):
    match num:
        case 0:
            return "the number is zero"
        case 1:
            return "the number is one"
        case -1: return "the num is -ve"
        case _ if num>1:
            return "the number is greater than one"
        case _ if num<-1:
            return "the number is less than -ve one"
        case _:
            return "the number is between -1 and 1 but zero"

numbers = [0,1,-1,5,-10,0.5]
for num in numbers:
    result = categorize_number(num)
    print(f"Number: {num} -> {result}")

# case _: The underscore _ is a wildcard pattern that matches any value. It’s used when you want to match any value but still need to apply some additional condition.