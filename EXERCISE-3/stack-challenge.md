## Challenge: Reverse "ICTRWANDA" using stack

**Algorithm Steps:**
1. Create an empty stack.
2. For each character in "ICTRWANDA", push it onto the stack.
3. Pop each character from the stack and append to result.

**Code:**
```python
stack = []
for char in "ICTRWANDA":
    stack.append(char)
reversed_str = ""
while stack:
    reversed_str += stack.pop()
print(reversed_str)  # Output: ADNATWC
```
**Explanation:**  
Each character is pushed, then popped in reverse order, producing "ADNAWTCI".