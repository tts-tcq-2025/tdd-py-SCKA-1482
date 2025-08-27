import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        delimiter, numbers_part = self._extract_delimiter(numbers)
        number_list = self._split_numbers(numbers_part, delimiter)
        self._check_negatives(number_list)
        filtered_numbers = self._filter_large_numbers(number_list)
        return sum(filtered_numbers)

    def _extract_delimiter(self, numbers: str):
        default_delimiters = [',', '\n']
        if numbers.startswith("//"):
            delimiter_part, numbers_part = numbers[2:].split('\n', 1)
            if delimiter_part.startswith("[") and delimiter_part.endswith("]"):
                delimiter = delimiter_part[1:-1]
            else:
                delimiter = delimiter_part
            return [delimiter], numbers_part
        else:
            return default_delimiters, numbers

    def _split_numbers(self, numbers_part: str, delimiters: list[str]):
        delimiters_pattern = '|'.join(re.escape(d) for d in delimiters)
        tokens = re.split(delimiters_pattern, numbers_part)
        return [int(token) for token in tokens if token != '']

    def _check_negatives(self, numbers: list[int]):
        negatives = [n for n in numbers if n < 0]
        if negatives:
            negatives_str = ", ".join(str(n) for n in negatives)
            raise ValueError(f"negatives not allowed: {negatives_str}")

    def _filter_large_numbers(self, numbers: list[int]) -> list[int]:
        return [n for n in numbers if n <= 1000]
