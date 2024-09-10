print("""
NOTE:
UNITS MUST BE IN GRAMS.""")
widgets_weight = 75
gizmos_weight = 112

widgets_num = int(input("Enter the number of widgets you want: "))
gizmos_num = int(input("Enetr the numver of gizmos you want: "))

total_price = (widgets_weight*widgets_num) + (gizmos_weight*gizmos_num)
print(f"""****************************************************
{widgets_num} widgets cost is {widgets_weight*widgets_num}
{gizmos_num} gizmos cost is {widgets_num*widgets_weight}
---------------------------------------------
Total cost is {total_price}
****************************************************""")