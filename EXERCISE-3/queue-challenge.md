## Challenge: Queue vs Stack for School Lunch Lines

**Algorithmic Comparison:**
- **Queue (FIFO):**
  1. Students join the end of the line.
  2. First student in line is served first.
  3. Each student is served in arrival order.

- **Stack (LIFO):**
  1. Students join the top of the stack.
  2. Last student to join is served first.
  3. Earlier students wait longer.

**Code Example (Queue):**
```python
lunch_queue = []
lunch_queue.append("Student1")
lunch_queue.append("Student2")
lunch_queue.append("Student3")
served = lunch_queue.pop(0)  # Student1 served first
```
**Explanation:**  
Queue is correct for fairness; stack would be unfair as last arrivals are served first.