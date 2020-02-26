import time
# todo get this in github
# todo Add audio instructions for each step


def alkalizing_your_blood():
    start = time.perf_counter()
    reached_oxygen_saturation = input("When you reach oxygen saturation press enter.")
    end = time.perf_counter()
    time_it_took_to_alkalize = end - start
    print(f"It took you {time_it_took_to_alkalize} seconds to reach oxygen")

    return time_it_took_to_alkalize


def hold_breath():
    start = time.perf_counter()
    breath_in = input("When you take a breathe in press enter.")
    end = time.perf_counter()
    duration_of_breath_hold = end - start
    print(f"You held your breath for {duration_of_breath_hold}seconds")

    return duration_of_breath_hold


def fiffteen_second_hold():
    start = time.perf_counter()
    print("hold breath")
    while start < 15:
        start = time.perf_counter()
    print("release breath")


def start_hoffing():
    hoffing = True
    input("press any button to start.")
    while hoffing:
        breathing_time = alkalizing_your_blood()
        hold_breath_time = hold_breath()
        fiffteen_second_hold()
        print(f"If took {breathing_time} to oxygen your blood")
        print(f"You held your breath for {hold_breath_time}")
        continue_hoffing = input("Whould you like to continue hoffing? y/n")
        if continue_hoffing == "n":
            hoffing = False


start_hoffing()


