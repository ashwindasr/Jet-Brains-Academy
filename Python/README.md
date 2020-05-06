## Notes

### Formatted string literals
Formatted string literals (or, simply, f-strings) are used to embed the values of expressions inside string literals. This way is supposed to be the easiest one: you only need to put f before the string and put the variables you want to embed into the string in curly braces. They are also the newest feature among all string formatting methods in Python.
```python
name = 'Elizabeth II'
title = 'Queen of the United Kingdom and the other Commonwealth realms'
reign = 'the longest-lived and longest-reigning British monarch'
f'{name}, the {title}, is {reign}.'
```
If you print this short string, you'll see an output that is five times longer than its representation in code:
```
Elizabeth II, the Queen of the United Kingdom and the other Commonwealth realms, is the longest-lived and longest-reigning British monarch.
```
You can also use different formatting specifications with f-literals, for example rounding decimals would look like this:
```python
hundred_percent_number = 1823
needed_percent = 16
needed_percent_number = hundred_percent_number * needed_percent / 100
 
print(f'{needed_percent}% from {hundred_percent_number} is {needed_percent_number}')
# 16% from 1823 is 291.68
 
print(f'Rounding {needed_percent_number} to 1 decimal place is {needed_percent_number:.1f}')
# Rounding 291.68 to 1 decimal place is 291.7
```
You can read more about Format Specification Mini-Language in Python in the [official documentation](https://docs.python.org/3.6/library/string.html#format-specification-mini-language).

Maybe, you'll think that these methods are not important and overrated but they give you the opportunity to make your code look fancy and readable.
