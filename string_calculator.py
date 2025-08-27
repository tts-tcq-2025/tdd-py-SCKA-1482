import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0

        delimiters = [",", "\n"]
        nums_str = numbers

        if numbers.startswith("//"):
            delimiter_part, nums_str = numbers.split("\n", 1)
            custom_delimiters = re.findall(r"\[(.*?)\]", delimiter_part)
            if custom_delimiters:
                delimiters = custom_delimiters
            else:
                delimiters = [delimiter_part[2:]]

        delimiter_pattern = "|".join(map(re.escape, delimiters))
        parts = re.split(delimiter_pattern, nums_str)

        negatives = []
        total = 0
        for part in parts:
            if part == "":
                continue
            num = int(part)
            if num < 0:
                negatives.append(num)
            elif num <= 1000:
                total += num

        if negatives:
            raise ValueError("negatives not allowed: " + ", ".join(str(n) for n in negatives))

        return total
