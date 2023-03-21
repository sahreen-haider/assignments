operators = {"1) Which is the correct operator for power(xy)?" : ["a) x^y" , "b) x**y" , "c) x^^y" , "d) None of the mentioned"],
            "2) Which one of these is floor division ?" : ["a) /" , "b) //" , "c) %" , "d) None of the mentioned"],
            "3) What is the answer of this expression, 22 % 3 is ?" : ["a) 7" , "b) 1" , "c) 0" , "d) 5"],
            "4) Mathematical operations can be performed on a string ?" : ["a) True" , "b) False"],
            "5) Operators with the same precedence are evaluated in which manner?" : ["a) Left to Right" , "b) Right to Left" , "c) Can't say" , "d) None of the mentioned"],
            "6) What is the output of this expression, 3*1**3?" : ["a) 27" , "b) 9" , "c) 3" , "d) 1"],
            "7) Which one of the following has the same precedence level?" : ["a) Addition and Subtracion" , "b) Multiplication , c) Division and Addition" , "d) Multiplication , Division , Addition and Subtraction" , "Addition and Multiplication"],
            "8) The expression Int(x) implies that the variable x is converted to integer." : ["a) True" , "b) False"],
            "9) Which one of the following has the highest precedence in the expression?" : ["a) Exponential" , "b) Addition" , "c) Multiplication" , "d) Parantheses"],
            "10) Which function overloads the >> operator?" : ["a) more()" , "b) gt()" , "c) ge()" , "d) None of the above"]}

operators_answers = ["b" , "b" , "b" , "b" , "a" , "c" , "a" , "a" , "d" , "d"]

lists = {"1) Which of the following commands will create a list?" : ["a) list1 = list()" , "b) list1 = []" , "c) list1 = list([1, 2, 3])" , "d) all of the mentioned"],
        "2) What is the output when we execute list(“hello”)?" : ["a) ['h','e','l','l','o']" , "b) ['hello']" , "c) ['llo']" , "d) ['olleh']"],
        "3) Suppose listExample is ['h','e','l','l','o'], what is len(listExample)?" : ["a) 5" , "b) 4" , "c) None" , "d) Error"],
        "4) Suppose list1 is [2445,133,12454,123], what is max(list1)?" : ["a) 2445" , "b) 133" , "c) 12454" , "d) 123"],
        "5) Suppose list1 is [3, 5, 25, 1, 3], what is min(list1)?" : ["a) 3" , "b) 5" , "c) 25" , "d) 1"],
        "6) Suppose list1 is [1, 5, 9], what is sum(list1)?" : ["a) 1" , "b) 9" , "c) 15" , "d) Error"],
        "7) To shuffle the list(say list1) what function do we use?" : ["a) list1.shuffle()" , "b) shuffle(list1)" , "c) random.shuffle(list1)" , "d) random.shuffleList(list1)"],
        "8) Suppose list1 is [4, 2, 2, 4, 5, 2, 1, 0], Which of the following is correct syntax for slicing operation?" : ["a) print(list1[2:])" , "b) print(list1[:2])" , "c) print(list1[:-2])" , "d) all of the mentioned"],
        "9)  Suppose list1 is [2, 33, 222, 14, 25], What is list1[-1]?" : ["a) Error" , "b) None" , "c) 25" , "d) 2"],
        "10) Suppose list1 is [2, 33, 222, 14, 25], What is list1[:-1]?" : ["a) [2, 33, 222, 14]" , "b) Error" , "c) 25" , "d) [25, 14, 222, 33, 2]"]}

lists_answers = ["d" , "a" , "a" , "c" , "d" , "c" , "c" , "d" , "c" , "a"]

file_handling = {"1) To open a file c:\scores.txt for reading, we use _____________?" : ["a) infile = open(“c:\scores.txt”, “r”)" , "b) infile = open(“c:\\scores.txt”, “r”)" , "c) infile = open(file = “c:\scores.txt”, “r”)" , "d) infile = open(file = “c:\\scores.txt”, “r”)"],
                "2) To open a file c:\scores.txt for writing, we use ____________?" : ["a) outfile = open(“c:\scores.txt”, “w”)" , "b) outfile = open(“c:\\scores.txt”, “w”)" , "c) outfile = open(file = “c:\scores.txt”, “w”)" , "d) outfile = open(file = “c:\\scores.txt”, “w”)"],
                "3) To open a file c:\scores.txt for appending data, we use ____________?" : ["a) outfile = open(“c:\\scores.txt”, “a”)" , "b) outfile = open(“c:\\scores.txt”, “rw”)" , "c) outfile = open(file = “c:\scores.txt”, “w”)" , "d) outfile = open(file = “c:\\scores.txt”, “w”)"],
                "4) Which of the following statements are true?" : ["a) When you open a file for reading, if the file does not exist, an error occurs" , "b) When you open a file for writing, if the file does not exist, a new file is created" , "c) When you open a file for writing, if the file exists, the existing file is overwritten with the new file" , "d) All of the mentioned"],
                "5) To read two characters from a file object infile, we use ____________?" : ["a) infile.read(2)" , "b) infile.read()" , "c) infile.readline()" , "d) infile.readlines()"],
                "6) To read the entire remaining contents of the file as a string from a file object infile, we use ____________?" : ["a) infile.read(2)" , "b) infile.read()" , "c) infile.readline()" , "d) infile.readlines()"],
                "7) To read the next line of the file from a file object infile, we use ____________?" : ["a) infile.read(2)" , "b) infile.read()" , "c) infile.readline()" , "d) infile.readlines()"],
                "8) To read the remaining lines of the file from a file object infile, we use ____________?" : ["a) infile.read(2)" , "b) infile.read()" , "c) infile.readline()" , "d) infile.readlines()"],
                "9) The readlines() method returns ____________?" : ["a) str" , "b) a list of lines" , "c) a list of single characters", "d) a list of integers"],
                "10) 4. Which one of the following is not attributes of file?" : ["a) closed" , "b) softspace" , "c) rename" , "d) mode"]}

file_handling_answers = ["b" , "b" , "a" , "d" , "a" , "b" , "c" , "d" , "b" , "c"]

classes_and_objects = {"1) The assignment of more than one function to a particular operator is _______?" : ["a) Operator over-assignment" , "b) Operator overriding" , "c) Operator overloading" , "d) Operator instance"],
                    "2) Which of the following is not a class method?" : ["a) Non-static" , "b) Static" , "c) Bounded" , "d) Unbounded"],
                    "3) What are the methods which begin and end with two underscore characters called?" : ["a) Special methods" , "b) In-built methods" , "c) User-defined methods" , "d) Additional methods"],
                    "4) Special methods need to be explicitly called during object creation." : ["a) True" , "b) False"],
                    "5) What is hasattr(obj,name) used for?" : ["a) To access the attribute of the object" , "b) To delete an attribute" , "c) To check if an attribute exists or not" , "d) To set an attribute"],
                    "6) What is delattr(obj,name) used for?" : ["a) To print deleted attribute" , "b) To delete an attribute" , "c) To check if an attribute is deleted or not" , "d) To set an attribute"],
                    "7) __del__ method is used to destroy instances of a class." : ["a) True" , "b) False"],
                    "8) What does print(Test.__name__) display (assuming Test is the name of the class)?" : ["a) ()" , "b) Exception is thrown" , "c) Test" , "d) __main__"],
                    "9) _____ represents an entity in the real world with its identity and behaviour." : ["a) A method" , "b) An object" , "c) A class" , "d) An operator"],
                    "10) _____ is used to create an object." : ["a) class" , "b) constructor" , "c) User-defined function]" , "d) In-built functions"]}

classes_and_objects_answers = ["c" , "a" , "a" , "b" , "c" , "b" , "a" , "c" , "b" , "b"]

oops = {"1) Which of the following best describes inheritance?" : ["a) Ability of a class to derive members of another class as a part of its own definition" , "b) Means of bundling instance variables and methods in order to restrict access to certain class members" , "c) Focuses on variables and passing of variables to functions" , "d) Allows for implementation of elegant software that is well designed and easily modified"],
        "2) Which of the following statements is wrong about inheritance?" : ["a) Protected members of a class can be inherited" , "b) The inheriting class is called a subclass" , "c) Private members of a class can be inherited and accessed" , "d) Inheritance is one of the features of OOP"],
        "3) All subclasses are a subtype in object-oriented programming" : ["a) True" , "b) False"],
        "4) When defining a subclass in Python that is meant to serve as a subtype, the subtype Python keyword is used." : ["a) True" , "b) False"],
        "5) Suppose B is a subclass of A, to invoke the __init__ method in A from B, what is the line of code you should write?" : ["a) A.__init__(self)" , "b) B.__init__(self)" , "c) A.__init__(B)" , "d) B.__init__(A)"],
        "6) What does built-in function type do in context of classes?" : ["a) Determines the object name of any value" , "b) Determines the class name of any value" , "c) Determines class description of any value" , "d) Determines the file name of any value"],
        "7) Which of the following is not a type of inheritance?" : ["a) Double-level" , "b) Multi-level" , "c) Single-level" , "d) Multiple"],
        "8) What does built-in function help do in context of classes?" : ["a) Determines the object name of any value" , "b) Determines the class identifiers of any value" , "c) Determines class description of any built-in type" , "d) Determines class description of any user-defined built-in type"],
        "9) What does single-level inheritance mean?" : ["a) A subclass derives from a class which in turn derives from another class" , "b) A single superclass inherits from multiple subclasses" , "c) A single subclass derives from a single superclass" , "d) Multiple base classes inherit a single derived class"],
        "10) Which of the following statements isn't true?" : ["a) A non-private method in a superclass can be overridden" , "b) A derived class is a subset of superclass" , "c) The value of a private variable in the superclass can be changed in the subclass" , "d) When invoking the constructor from a subclass, the constructor of superclass is automatically invoked"]}

oops_answers = ["a" , "c" , "b" , "b" , "a" , "b" , "a" , "c" , "c" , "c"]