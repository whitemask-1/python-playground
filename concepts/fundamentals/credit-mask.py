card_number = "455568488392"
masked = "#" * (len(card_number) - 4) + card_number[-4:]
print(masked)
