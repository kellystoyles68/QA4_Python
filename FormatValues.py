# In-class exercise to create a module of functions
# that can be used to format values and dates.
#
# To use the module set up the following statement
# at the beginning of another program:
#    import FormatValues
#

def PrecentNumber (NumberValue):
    # Function will accept a value and format to a precent ###%. 
    NumberValueStr = "{:.2%}".format(NumberValue)
    
    return NumberValueStr

def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "{:,.2f}".format(DollarValue)

    return DollarValueStr


def FComma0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "{:,.0f}".format(DollarValue)

    return DollarValueStr


def FNumber0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "{:.0f}".format(DollarValue)

    return DollarValueStr


def FNumber2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "{:.2f}".format(DollarValue)

    return DollarValueStr


def FDateShort(DateValue):
    # Function will accept a value and format it to yyyy-mm-dd.

    DateValueStr = DateValue.strftime("%Y-%m-%d")

    return DateValueStr


def FDateMedium(DateValue):
    # Function will accept a value and format it to dd-Mon-yy.

    DateValueStr = DateValue.strftime("%d-%b-%y")

    return DateValueStr


def FDateLong(DateValue):
    # Function will accept a value and format it to Weekday, Month dd, yyyy.

    DateValueStr = DateValue.strftime("%A, %B %d, %Y")

    return DateValueStr