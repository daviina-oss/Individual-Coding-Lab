"""
road_simulation.py
Full Self Driving Simulation mode in Kigali: ALU Rwanda -> Convention Center
Your job: complete TODO 1 to TODO 10 below (replace each `pass`).
Do NOT edit engine.py, index.html or transit_program.py.
Run with: python road_simulation.py or python3 road_simulation.py
"""

SEGMENT_M = 100
ZEBRA_WAIT = 15
ACCELERATION = 5
BRAKING = 20
START_NAME = "ALU Rwanda"
END_NAME = "Convention Center"

# Each item in the road list is ONE segment of road. On the screen each segment
# is 100 m long
road = [
    "60", "road", "road", "road", "zebra", "road", "road",
    "80", "road", "road", "road", "road", "road", "road",
    "bus", "road", "road", "bus", "road", "road", "road",
    "60", "road", "road", "road", "road", "80", "road",
    "road", "zebra", "road", "road", "road", "road",
]


# ==================== PART 1: CHECK THE SIGN ====================

# TODO 1: Return True only if sign is text AND is "bus", "zebra",
# or a number from 20 to 100 written as text (e.g. "80"). Otherwise False.
def is_valid_sign(sign):
    # 1. Only text can be a sign
    if not isinstance(sign, str):
        return False
    # 2. "bus" and "zebra" are always allowed
    if sign == "bus" or sign == "zebra":
        return True
    # 3. A speed sign is a whole number written as text, from 20 to 100
    if sign.isascii() and sign.isdigit():
        return 20 <= int(sign) <= 100
    # 4. Anything else is not allowed
    return False


# TODO 2: Return "bus", "zebra", "speed" (a number) or "road" (anything else).
def get_sign_type(sign):
    # 1. Anything that is not text is just road
    if not isinstance(sign, str):
        return "road"
    # 2. Check the special signs
    if sign == "bus":
        return "bus"
    if sign == "zebra":
        return "zebra"
    # 3. A number written as text is a speed sign
    if sign.isascii() and sign.isdigit():
        return "speed"
    # 4. Everything else is plain road
    return "road"


# ==================== PART 2: TAKE ACTION ====================

# TODO 3: If the sign is a speed sign, return its number as an int. Else return
# current_limit.
def get_speed_limit(sign, current_limit):
    # 1. A speed sign sets a new limit
    if get_sign_type(sign) == "speed":
        return int(sign)
    # 2. Any other sign keeps the current limit
    return current_limit


# TODO 4: Return 0 while stop_timer is above 0, otherwise return limit.
def get_target_speed(limit, stop_timer):
    # 1. Waiting at a zebra crossing: the target speed is 0
    if stop_timer > 0:
        return 0
    # 2. Otherwise drive at the speed limit
    return limit


# TODO 5: Move speed ONE step towards target and return it.
# Below target: add ACCELERATION (never go above target).
# Above target: subtract BRAKING (never go below target).
def adjust_speed(speed, target):
    # 1. Too slow: speed up, but never above the target
    if speed < target:
        speed = speed + ACCELERATION
        if speed > target:
            speed = target
    # 2. Too fast: brake, but never below the target
    elif speed > target:
        speed = speed - BRAKING
        if speed < target:
            speed = target
    # 3. Return the new speed
    return speed


# TODO 6: Use a loop. Return (speed_signs, zebras, buses).
def count_signs(road_list):
    # 1. Start every counter at zero
    speed_signs = 0
    zebras = 0
    buses = 0
    # 2. Look at every segment and count its type
    for sign in road_list:
        sign_type = get_sign_type(sign)
        if sign_type == "speed":
            speed_signs = speed_signs + 1
        elif sign_type == "zebra":
            zebras = zebras + 1
        elif sign_type == "bus":
            buses = buses + 1
    # 3. Return the three counts
    return speed_signs, zebras, buses


# ==================== PART 3: SAFE INPUT AND JOURNEY SUMMARY ====================

# TODO 7: Keep asking until the user types a whole number from low to high.
# Use try/except for text that is not a number. Return the number as an int.
def ask_for_number(question, low, high):
    while True:
        # 1. Ask, and turn the answer into a whole number
        try:
            number = int(input(question))
        except ValueError:
            # 2. Text (or a decimal) is not allowed: ask again
            print(f"  That is not a whole number. Type a number from {low} to {high}.")
            continue
        # 3. Accept the number only if it is inside the range
        if low <= number <= high:
            return number
        print(f"  Out of range. Type a number from {low} to {high}.")


# TODO 8: Insert sign at position. Return False if position is not from 0 to
# len(road_list).
# Otherwise insert and return True.
def insert_sign(road_list, sign, position):
    # 1. Refuse a position outside 0 to len(road_list)
    if not isinstance(position, int) or position < 0 or position > len(road_list):
        return False
    # 2. Insert the sign and report success
    road_list.insert(position, sign)
    return True


# TODO 9: Replace the sign at index with a new sign. Return False if index is not
# from 0 to len(road_list) - 1. Otherwise replace it and return True.
def replace_sign(road_list, sign, index):
    # 1. Refuse an index outside 0 to len(road_list) - 1
    if not isinstance(index, int) or index < 0 or index > len(road_list) - 1:
        return False
    # 2. Replace the sign and report success
    road_list[index] = sign
    return True


# TODO 10: Summarise the journey. Use a loop to count the signs we pass
# (every segment that is not "road"). Return four values:
# (signs_passed, length_m, START_NAME, END_NAME)
# length_m is the number of segments times SEGMENT_M.
def get_journey_summary(road_list):
    # 1. Count every segment that is not plain road
    signs_passed = 0
    for sign in road_list:
        if sign != "road":
            signs_passed = signs_passed + 1
    # 2. Work out the road length in metres
    length_m = len(road_list) * SEGMENT_M
    # 3. Return the summary
    return signs_passed, length_m, START_NAME, END_NAME


if __name__ == "__main__":
    import sys
    import transit_program
    transit_program.run(sys.modules[__name__])
