'''
#
Q 12 Create a tuple containing the names of five countries and display the whole tuple. Ask
     the user to enter one of the countries that have been shown to them and then display
     the index number (i.e. position in the list) of that item in the tuple.
'''
countries = ("INDIA", "IRAN" , "JAPAN", "RUSSIA", "USA")
print(countries)
if __name__ == "__main__":
    name = input("Enter country name: ").upper()
    if name in countries:
        print(f"{countries.index(name)} ---> {name}")
