import random
user_status = random.choice(["admin", "user", "goust", "unknown"])
match user_status:
    case "admin":
        print("Free access")
    case "user":
        print("Access restricted")
    case "goust":
        print("Viewing only")
    case "unknown":
        print("Access denied")


