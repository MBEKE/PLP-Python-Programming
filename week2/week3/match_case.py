# EXPAMPLE
def Weekday(n):
    match n:
        case 0: return "Monday"
        case 1: return "Tuesday"
        case 2: return "Wednesday"
        case 3: return "Thursday"
        case 4: return "Friday"
        case 5: return "Saturday"
        case 6: return "Sunday"
        case _: return "Invalid day number"
print(Weekday(3))
print(Weekday(6))
print(Weekday(7))

# Combined Cases in Match Statement
def access(user):
    match user:
        case "admin" | "manager": return "Full access"
        case "Guest": return "Limited access"
        case _: return "No access"
print(access("manager"))
print(access("Guest"))
print(access("Ogada"))

# List as the Argument int Match Case Statement
def greeting(details):
    match details:
        case [time, name]:
            return f'Good {time} {name}!'
        case [time, *names]:
            msg = ''
            for name in names:
                msg += f'Good {time} {name}!\n'
            return msg
print(greeting(['Morning', 'Ogada']))
print(greeting(['Afternoon', 'Guest']))
print(greeting(['Evening', 'Kajal', 'Praveen', 'Lata']))

# 'if' in 'Case' Clause
def intr(details):
    match details:
        case [amt, duration] if amt < 10000:
            return amt * 10 * duration / 100
        case [amt, duration] if amt >= 10000:
            return amt * 15 * duration / 100
print("Interest = ", int([5000, 5]))
print("Interest = ", int([1500, 3]))