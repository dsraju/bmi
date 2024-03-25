import argparse

class Bmi:
    """
    BMI Calculator.
    """

    def __init__(self, weight=150, height=70, verbose=False):
        """
        Initializes an instance of Bmi.

        Args:
            weaight (int): Weaight in LB
            height  (int): Height in Inches
            verbose  (bool): Output to have More verbose message
        """
        self.weight_in_lb = weight
        self.height_in_inch = height
        self.verbose = verbose

    def calaculate_bmi(self):
        """
        Calculate BMI.

        Returns:
            str: A message indicating BMI and weight in KG.
        """
        w = self.weight_in_lb
        h = self.height_in_inch
        # Add your action implementation here
        if self.verbose:
          message = f"Height {h}In Weight in {w}LB {w/2.2046:.2f}KG {703*w/h**2:.2f}BMI"
        else:
          message = f"Weight in {w}LB {w/2.2046:.2f}KG {703*w/h**2:.2f}BMI"
        return message

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description='MyClass Example')

    # Add arguments
    parser.add_argument('-w', '--weight', type=float, help='Weight in LB')
    parser.add_argument('-i', '--height', type=float, help='Height in Inches')
    parser.add_argument('-v', '--verbose', action='store_true')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Create an instance of Bmi
    weight = args.weight or 135
    height = args.height or 68
    my_bmi = Bmi(weight, height, args.verbose)

    # Perform the action
    result = my_bmi.calaculate_bmi()

    # Print the result
    print(result)

if __name__ == '__main__':
    main()

