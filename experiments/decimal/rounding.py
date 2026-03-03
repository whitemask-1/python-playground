from decimal import Decimal, localcontext, BasicContext, ROUND_HALF_UP

num = 1.9374
print(Decimal(num).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

print(Decimal("1") / Decimal("3"))

with localcontext() as ctx:
    ctx.prec = 4
    print(Decimal("1") / Decimal("3"))


def round_to_2(n):
    with localcontext(BasicContext):
        return round(Decimal(n), 3)


print(round_to_2(num))
