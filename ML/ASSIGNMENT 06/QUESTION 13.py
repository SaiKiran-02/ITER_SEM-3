'''
#
Q 13 Write a Python function that takes two files of equal size as input from the user. The first
     file contains weights of items, and the second file contains corresponding prices. Create
     another file that should contain price per unit weight for each item.
'''
def calculate_price_per_unit_weight(weights_file, prices_file, output_file):
    try:
        with open(weights_file, 'r') as wf:
            weights = [float(line.strip()) for line in wf if line.strip()]

        with open(prices_file, 'r') as pf:
            prices = [float(line.strip()) for line in pf if line.strip()]

        if len(weights) != len(prices):
            print("Error: The two files must contain the same number of entries.")
            return

        price_per_unit_weight = [price / weight if weight != 0 else 0 for price, weight in zip(prices, weights)]

        with open(output_file, 'w') as of:
            for ppuw in price_per_unit_weight:
                of.write(f"{ppuw}\n")

        print(f"Price per unit weight has been written to {output_file}.")

    except FileNotFoundError as e:
        print(f"File not found: {e}")
    except ValueError:
        print("Error: Please ensure that the files contain valid numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")

