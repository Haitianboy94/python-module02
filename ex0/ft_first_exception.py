def check_temperature(temp_str):

    try:
        new_tmp = int(temp_str)
        if new_tmp >= 0 and new_tmp <= 40:
            return f"Temperature {new_tmp}°C is perfect for plants"
        elif new_tmp < 0:
            return f"Error: {new_tmp}°C is too cold for plants (min 0°C)"
        elif new_tmp > 40:
            return f"Error: {new_tmp}°C is too hot for plants (max 40°C)"
    except ValueError:
        return f"{temp_str} is not a valid number"


def test_temperature_input():
    check_with_good = 25
    print(f"Testing temperature: {check_with_good}\n"
          f"{check_temperature(check_with_good)}\n")
    check_with_bad = "abc"
    print(f"Testing temperature: {check_with_bad}\n"
          f"{check_temperature(check_with_bad)}\n")
    check_extrem_posi = 100
    print(f"Testing temperature: {check_extrem_posi}\n"
          f"{check_temperature(check_extrem_posi)}\n")
    check_extrem_nega = -50
    print(f"Testing temperature: {check_extrem_nega}\n"
          f"{check_temperature(check_extrem_nega)}\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    test_temperature_input()
