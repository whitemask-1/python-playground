year = 2006
month = 3
day = 18
hour = 18
minute = 54
second = 1

if (  # Indentation block used to compute indentation level
    1900 < year < 2100
    and 1 <= month <= 12
    and 1 <= day <= 31
    and 0 <= hour < 24
    and 0 <= minute < 60
    and 0 <= second < 60
):
    print("Valid date")

list = [5, 0, 2, 3]
# Blank Line <- ignored by lexical analyzer
for idx, i in enumerate(list):

    # INDENT TOKEN
    print(idx, i)
# DEDENT TOKEN

print(
    input("Whats your name?")
)  # <- Generates an ENDMARKER TOKEN after interactive input

# False, None, True
# and as or if is in try while with
# pass raise return assert async await
# lambda global nonlocal break class
# def elif not yield except del finally
#
