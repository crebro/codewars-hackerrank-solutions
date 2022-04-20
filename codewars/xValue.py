def solveBetter(eq: str):
    a, b = eq.replace("x", "0").split("=")
    x = eval(a) - eval(b)
    if "- x" in eq:
        x = -x
    return x if eq.find("x") > eq.find("=") else -x


# Value of X Codewars Solution - Submitted by [Kreation Duwal]
def solve(eq: str):
    # splits the equation into left hand side or right hand side
    equationSplit = eq.split("=")
    lhs = equationSplit[0]
    rhs = equationSplit[1]

    def calculateX(xIncludedString, xExcludedString):
        # finds x in the side that consists of x
        xIndex = xIncludedString.find("x")
        xExcludedValue = eval(xExcludedString)
        xHasMinus = xIndex >= 2 and xIncludedString[xIndex - 2] == "-"
        try:
            # Calculates return value by subtracting the evaluation of the string with x from the evaulation of the string without x
            # This may cuase error when x is present singly, hence error handling is done
            returnValue = xExcludedValue - eval(
                f"{xIncludedString[0: xIndex - 2 if xIndex >= 2 else xIndex  ]} {xIncludedString[xIndex + 1:]}"
            )
            # if x consists of a "-" sign then send it towards the other side
            return returnValue if not (xHasMinus) else -returnValue
        except Exception:
            return xExcludedValue if not (xHasMinus) else -xExcludedValue

    if "x" in lhs:
        return calculateX(lhs, rhs)
    return calculateX(rhs, lhs)
