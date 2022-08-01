print("""
TRUTH TABLES (Logic Gates)

and or not
!= (not equal)
== (equal)
>= (greater than or equal)
<= (less than or equal)
True False

Logic Gates

(NOT) not - performs the opposite action
not False       True
not True        False
_______________________

(OR) or - True unless F/F
True or False   True
True or True    True
False or True   True
False or False  False

(AND) and - False unless T/T
True and False  False
True and True   True
False and True  False
False and False False

(NOR) not or - False unless F/F
not (True or False)     False
not (True or True)      False
not (False or True)     False
not (False or False)    True

(NAND) not and 0 True unless T/T
not (True and False)    True
not (True and True)     False
not (False and True)    True
not (False and False)   True

_______________________

(!=) not equal
1 != 0      True
1 != 1      False
0 != 1      True
0 != 0      False

(==) equal
1 == 0      False
1 == 1      True
0 == 1      False
0 == 0      True
""")