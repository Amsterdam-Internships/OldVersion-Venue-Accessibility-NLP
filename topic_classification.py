def topic_classification(text):

    general = ["wheelchair", "disability", "disabled", "handicap", "handicapped", "mobility"]
    entrance = ["entrance", "door", "ramp", "narrow"]
    bathroom = ["toilet", "bathroom", "restroom"]
    transport = ["parking"]
    stairs = ["elevator", "steps", "stair", "steep", "narrow"]
    space = ["cramped", "spacious"]
    staff = ["service", "staff", "waiter", "waitress"]

    category = str()

    if any(word in text for word in general):
        category = category + "general"
    elif any(word in text for word in entrance):
        category = category + "entrance"
    elif any(word in text for word in bathroom):
        category = category + "bathroom"
    elif any(word in text for word in transport):
        category = category + "transport"
    elif any(word in text for word in stairs):
        category = category + "stairs"
    elif any(word in text for word in space):
        category = category + "space"
    elif any(word in text for word in staff):
        category = category + "staff"


def topic_bool(text):
    
    if text == "general":
        category_id = 1
    elif text == "entrance":
        category_id = 2
    elif text == "bathroom":
        category_id = 3
    elif text == "transport":
        category_id = 4
    elif text == "stairs":
        category_id = 5
    elif text == "space":
        category_id = 6
    elif text == "staff":
        category_id = 7
    
    return category_id
          