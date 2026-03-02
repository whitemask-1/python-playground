def encode(strs: list[str]) -> str:
    encoded = "".join(f"{len(s)}#{s}" for s in strs)
    return encoded


def decode(s: str) -> list[str]:
    decoded = []
    i = 0
    while i < len(s):
        j = s.find("#", i)
        length = int(s[i:j])
        decoded.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length

    return decoded


test = ["Hello", "World"]
encoded_test = encode(test)
decoded_test = decode(encoded_test)

print(test, encoded_test, decoded_test)
