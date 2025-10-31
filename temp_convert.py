# TODO: complete the function definition in the next line
def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit.
    @param celsius (float): Temperature in Celsius.
    @return (float) equivalent temperature in F
    """
    return 9 / 5 * celsius + 32


# TODO: complete the function definition in the next line
def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit temperature to Celsius.
    @param fahrenheit (float): Temperature in Fahrenheit.
    @return float: Equivalent temperature in Celsius.
    """
    return 5 / 9 * (fahrenheit - 32)


def main():
    c = 36.5
    print(celsius_to_fahrenheit(c))

    f = 101.3
    print(fahrenheit_to_celsius(f))


if __name__ == "__main__":
    main()
