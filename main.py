# DEFINE YOUR FUNCTIONS HERE!

# PART A: No argument & no return
def cook_toast():
    print("Get as much bread as you want.")
    print("Put the bread in the toaster.")
    print("Make sure your toaster is set to toast and select the darkness.")

def fire_alarm():
    print("BEEP. BEEP. BEEP.")
    print("SMOKE DETECTED.")
    print("Your toast is burnt.")

# PART B: Argument & no return
def spreads(topping1, topping2):
    print(f"First Topping: {topping1}")
    print(f"Second Topping: {topping2}")

# PART C: Argument & return
def spread_toast(spread1, spread2):
    return f"Half of your burnt toast has {spread1}, and the other half has {spread2}"

# PART D: Optional arguments
def side_dish(sideplate="raspberries"):
    print(f"Your toast now has a side of {sideplate}.")

# PART E: Review challenge
def make_toast():
    cook_toast()
    fire_alarm()
    spread_toast("honey", "butter")
    side_dish("fruit salad")
    print(f"Congratulations, you've made burnt toast with {spread1} and {spread2} and a side of {sideplate}!")


def main():
    print("hello world")
    # CALL YOUR FUNCTIONS in the main here
    cook_toast()
    fire_alarm()
    spreads("honey", "butter")
    print(spread_toast( "cream cheese", "jelly"))
    side_dish()
    side_dish("strawberries")



if __name__ == "__main__":
    main()


