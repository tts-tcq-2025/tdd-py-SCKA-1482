import re

class StringCalculator:

    def add(self, numbers: str) -> int:
        delimiters, nums = self._extract_delimiter(numbers)
        numbers_list = self._split_numbers(nums, delimiters)
        self._validate_negatives(numbers_list)
        numbers_filtered = self._filter_large_numbers(numbers_list)
        return sum(numbers_filtered)

    def _extract_delimiter(self, numbers: str):
        if numbers.startswith("//"):
            delimiter_line, rest = numbers[2:].split('\n', 1)
            delimiters = self._parse_delimiter_line(delimiter_line)
            return delimiters, rest
        return [",", "\n"], numbers

    def _parse_delimiter_line(self, delimiter_line: str):
        if delimiter_line.startswith("[") and delimiter_line.endswith("]"):
            return [delimiter_line[1:-1]]
        return [delimiter_line]

    def _split_numbers(self, numbers: str, delimiters: list[str]) -> list[int]:
        pattern = '|'.join(map(re.escape, delimiters))
        tokens = re.split(pattern, numbers)
        return [int(t) for t in tokens if t]

    def _validate_negatives(self, numbers: list[int]):
        negatives = self._find_negatives(numbers)
        self._raise_if_negatives(negatives)

    def _find_negatives(self, numbers: list[int]) -> list[int]:
        return [n for n in numbers if n < 0]

    def _raise_if_negatives(self, negatives: list[int]):
        if negatives:
            raise ValueError("negatives not allowed: " + ", ".join(map(str, negatives)))

    def _filter_large_numbers(self, numbers: list[int]) -> list[int]:
        return [n for n in numbers if n <= 1000]
