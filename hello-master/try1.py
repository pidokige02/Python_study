s = "123"

try:
    print(int(s) + 1)
    print(int(s) / 1)

except ValueError as ve:
    print("ValueError occurs!!!", ve)

except ZeroDivisionError as e:
    print("ZeroDivisionError occurs!!!", e)

except:
    print("Error occurs!!!")

else:
    print("elseeeeeeeeeeeeeee")

finally:
    print("ASDFAFSAFDAS")
