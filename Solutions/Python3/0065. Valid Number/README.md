# Solution Walk Through
Question: https://leetcode.com/problems/valid-number/

## Intuition
Use a regex.

## Approach
- Search if the string matches the regex.
- Regex explination: "^[-+]?(\d+(\.\d*)?|\.\d+)([eE][-+]?\d+)?$"
- Anchors: "^" and "$":

These symbols are placed at the start and end of the regex respectively to ensure the entire string matches the pattern within.

- Sign: "[-+]?"

This is an optional condition to check if the string has a "+" or "-" at the beginning.

- Integer/Decimal: "(\d+(\.\d*)?|\.\d+)"

**First half:** "\d+(\.\d*)?"

"\d+" matches one or more digits

"(\.\d*)?" gives the option for a decimal after the number

"|" OR operator seperating the first half from the second half

**Second half:** "\.\d+"

"\.\d+" matches a number where it begins with a decimal, such as ".97"

- Exponent: "([eE][-+]?\d+)?"

"[eE]" matches an e or E to begin the sequence

"[-+]?" is again the optional sign

"\d+" matches one or more digits

"?" at the end represents this entire portion being optional

- All together, this regex covers every possible case.

## Time Complexity
$O(n)$

## Space Complexity
$O(n)$