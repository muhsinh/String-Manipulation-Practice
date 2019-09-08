# Enter Word Below
myString="Abrakadabra"

#Part 1: Print third character of string
print(myString[2])

#Part 2: Print second to last character of string
n = len(myString)
print(myString[n-2])

#Part 3: Print first 5 characters of string
if n < 5:
    print("String too small")

substr3 = myString[0:4]
print(substr3)

#Part 4: Print all but last two characters of string 
part4 =(n-3)
substr4 = myString[0:part4]
print(substr4)

#Part 5: Print all the characters of this string with even indices (start at 0)
part5 = myString[::2]
print(part5)

#Part 6: Print all the characters of this string with odd indices (start at 1)
part6 = myString[1::2]
print(part6)

#Part 7: Print all the characters of the string in reverse order
part7 = myString[::-1]
print(part7)

#Part 8: rint every second character of the string in reverse order
part8 = myString[::-2]
print(part8)

#Part 9: print the length of the given string.
n= len(myString)
print(n)
