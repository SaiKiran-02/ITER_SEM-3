'''
#
Q 14 What will be the output produced on executing function inverse1 when the following input
     is entered as the value of variable num:
        (a)5    (b)0    (c)2.0    (d)x    (e)None

     Def inverse1():
     try:
     num = input(’Enter the number: ’)
     num = float(num)
     inverse = 1.0 / num
     except ValueError:
     print(’ValueError’)
     except TypeError:
     print(’TypeError’)
     except ZeroDivisionError:
     print(’ZeroDivisionError’)
     except:
     print(’Any other Error’)
     else:
     print(inverse)
     finally:
     print(’Function inverse completed’)
'''

def inverse1():
     try:
        num = input('Enter the number: ')
        num = float(num)
        inverse = 1.0 / num
     except ValueError:
        print('ValueError')
     except TypeError:
        print('TypeError')
     except ZeroDivisionError:
        print('ZeroDivisionError')
     except:
        print('Any other Error')
     else:
        print(inverse)
     finally:
        print('Function inverse completed')

inverse1()
