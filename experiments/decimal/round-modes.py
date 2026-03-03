import decimal as dec


def rounding_05UP(num):
    return dec.Decimal(num).quantize(dec.Decimal("0.01"), rounding=dec.ROUND_05UP)


def rounding_CEIL(num):
    return dec.Decimal(num).quantize(dec.Decimal("0.01"), rounding=dec.ROUND_CEILING)


def rounding_FLOOR(num):
    return dec.Decimal(num).quantize(dec.Decimal("0.01"), rounding=dec.ROUND_FLOOR)


def rounding_UP(num):
    return dec.Decimal(num).quantize(dec.Decimal("0.01"), rounding=dec.ROUND_UP)


def rounding_DOWN(num):
    return dec.Decimal(num).quantize(dec.Decimal("0.01"), rounding=dec.ROUND_DOWN)


def rounding_HALF_EVEN(num):
    return dec.Decimal(num).quantize(dec.Decimal("0.01"), rounding=dec.ROUND_HALF_EVEN)


def rounding_HALF_DOWN(num):
    return dec.Decimal(num).quantize(dec.Decimal("0.01"), rounding=dec.ROUND_HALF_DOWN)


def rounding_HALF_UP(num):
    return dec.Decimal(num).quantize(dec.Decimal("0.01"), rounding=dec.ROUND_HALF_UP)


float_list = [4.350, 5.2301, 3453.2041, 12.254, 1245.2532, 12.23, 1842.159]
for n in float_list:
    print(
        rounding_05UP(n),
        rounding_CEIL(n),
        rounding_FLOOR(n),
        rounding_UP(n),
        rounding_DOWN(n),
        rounding_HALF_EVEN(n),
        rounding_HALF_DOWN(n),
        rounding_HALF_UP(n),
    )
