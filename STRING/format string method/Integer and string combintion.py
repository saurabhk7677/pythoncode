print("hello my name is {}".format("saurabh"))
print("{} {}".format(10,"saurabh"))                                     # 10 is a string type dfault data because data type is not mentioned
print("{0} {1}".format(10,"saurabh"))                                   # {0} this is zero index = 10 &  {1} this is  one index = "saurabh"
print("{1} {0}".format(10,"saurabh"))                                   # same indexing on line 3 as a print.
print("{str1} {num1}".format(num1=10,str1="saurabh"))