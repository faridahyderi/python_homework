# Write your code here.

# TASK 1
def hello():
    return "Hello!"

print(hello())

# Task 2
def greet(name):
    return "Hello, " +name+ "!"

print(greet("Farida"))

#Task 3
def calc(a, b, str_operation="multiply"):
    try:
        match str_operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"


print(calc(3,4))
print(calc(3,4,"power"))
print(calc(14,0,"divide"))
print(calc(3,"4","add"))

#Task 4
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                return f"Invalid data type: {data_type}"
    except (ValueError, TypeError):
        return f"You can't convert {value} into a {data_type}."
    
print(data_type_conversion("546", "int"))
print(data_type_conversion("546", "float"))
print(data_type_conversion("hello", "int"))
print(data_type_conversion("12", "bool"))

#Task 5
def grade(*args):
    try:
        if not args:
            return "No grades provided."
        
        average = sum(args) / len(args)
        
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ValueError):
        return "Invalid data was provided."


print(grade(50, 25, 10))            
print(grade(60, 70, 65))            
print(grade(100, "90", 80))         
print(grade())                      
print(grade(90,80,95))           

# task 6
def repeat(string,count):
    string1=""
    for i in range(count):
        string1 +=string
    return string1

print(repeat("Hello",1))
print(repeat("hi",3))

#Task 7
def student_scores(pos_parameter, **kwargs):
    if not kwargs:
        return "No scores provided."
    
    if pos_parameter == "best":
        # Find the name of student with the highest score
        name_best_student = max(kwargs, key=kwargs.get)
        return name_best_student
    
    elif pos_parameter == "mean":
        # Calculate the average score
        average_score = sum(kwargs.values()) / len(kwargs)
        return average_score
    
    else:
        return "Invalid mode"

print(student_scores("best", Aaa=90, Bbb=85, Ccc=92, Ddd=98))
print(student_scores("mean", Aaa=78, Bbb=82))
print(student_scores("random", Aaa=90, Bbb=85))

#Task 8
def titleize(text):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()

    for i, word in enumerate(words):
        # Capitalize the first and last word OR if the word is not a 'little word'
        if i == 0 or i == len(words) - 1 or word not in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()
    
    return " ".join(words)

print((titleize("hello world")))
print((titleize("a long part of the story")))

#Task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter  
        else:
            result += "_"     
    
    return result

print(hangman("alphabet","ab"))

#Task 10
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()  
    pig_latin_words = []
    
    for word in words:
        if word.startswith("qu"):  # Special case for "qu" at the beginning
            pig_latin_words.append(word[2:] + "quay")
        else:
            index = 0
            while index < len(word) and word[index] not in vowels:
                # Handle "qu" together even after initial consonants
                if word[index:index + 2] == "qu":
                    index += 2
                    break
                index += 1
            pig_latin_words.append(word[index:] + word[:index] + "ay")
    
    return " ".join(pig_latin_words)  # Join the words back into a sentence

    
print(pig_latin("abbbb"))
print(pig_latin("bcdea"))
print(pig_latin("quit"))