'''
#
Q 12 Although electronic deposit has become extremely popular, payroll and accounts payable
     applications often print checks. A serious problem is the intentional alteration of a check
     amount by someone who plans to cash a check fraudulently.

     To prevent a dollar amount from being altered, some computerized check-writing systems
     employ a technique called check protection. Checks designed for printing by computer
     typically contain a fixed number of spaces for the printed amount. Suppose a paycheck
     contains eight blank spaces in which the computer is supposed to print the amount of a
     weekly paycheck. If the amount is large, then all eight of the spaces will be filled:
            1,230.60 (check amount)
            --------
            01234567 (position numbers)

     On the other hand, if the amount is smaller, then several of the spaces would ordinarily
     be left blank. For example,
            399.87
            --------
            01234567
     contains two blank spaces. If a check is printed with blank spaces, it’s easier for someone
     to alter the amount. Check-writing systems often insert leading asterisks to prevent
     alteration and protect the amount as follows:
            **399.87
            --------
            01234567


     Write a script that inputs a dollar amount, then prints the amount in check-protected
     format in a field of 10 characters with leading asterisks if necessary.
     [[Hint: In a format string that explicitly specifies alignment with <, ^ or >, you can precede
     the alignment specifier with the fill character of your choice.]]
'''