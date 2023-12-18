import math
try:
    imp = "import " + input("Enter the module you want to import: ")
    exec(imp)
    n={}
    n1, n2, k1, k2 = eval(input("Enter the n1,n2, k1, k2 with comma separation: "))
    n[k1] = n1
    n[k2] = n2
    k1, k2 = eval(input("Enter k1 and k2 with a comma in between: "))
    result = n[k1]/n[k2]
    m = int(input("Enter one more number: "))
    print("Result is:", result / math.sqrt(m))
    if (n[k1] == 0):
        raise RuntimeError
except ValueError:
    print("invalid literal")
except ZeroDivisionError:
    print("cannot be divided by 0")
except ImportError:
    print("module not found")
except SyntaxError:
    print("Something is missing")
except RuntimeError:
    print("May be meaningless")
except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
except KeyError:
    print("Requested was not found")
except:
    print("Something is wrong with the input")
else:
    print("No exception")
finally:
    print("Final call executed")