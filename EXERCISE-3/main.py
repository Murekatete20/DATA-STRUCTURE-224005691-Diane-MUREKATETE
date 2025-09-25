# ================================
# DATA STRUCTURE - BIT - EXERCISE NO:4
# Stack & Queue Practical + Challenge Questions
# ================================

from collections import deque

print("=====================================")
print("STACK QUESTIONS")
print("=====================================")

# -------------------------------
# Practical 1: MoMo push & undo
# -------------------------------
stack = []
stack.append("PIN")
stack.append("Amount")
stack.append("Confirm")
print("\n[Stack Practical 1]")
print("Stack after pushes:", stack)

stack.pop()  # Undo last
print("Stack after undo:", stack)

# -------------------------------
# Practical 2: UR pushes topics
# -------------------------------
stack = []
stack.append("Topic1")
stack.append("Topic2")
stack.append("Topic3")
print("\n[Stack Practical 2]")
print("Initial Stack:", stack)

stack.pop()
stack.pop()
print("Stack after popping two:", stack)
print("Top element now:", stack[-1])

# -------------------------------
# Challenge: Reverse "ICTRWANDA"
# -------------------------------
word = "ICTRWANDA"
stack = []

for ch in word:
    stack.append(ch)

reversed_word = ""
while stack:
    reversed_word += stack.pop()

print("\n[Stack Challenge]")
print("Original:", word)
print("Reversed:", reversed_word)

print("\n=====================================")
print("QUEUE QUESTIONS")
print("=====================================")

# -------------------------------
# Practical 1: Nyabugogo buses
# -------------------------------
queue = deque(["Bus1", "Bus2", "Bus3", "Bus4", "Bus5", "Bus6", "Bus7"])
print("\n[Queue Practical 1]")
print("Initial Queue:", queue)

for _ in range(5):  # 5 depart
    queue.popleft()

print("Queue after 5 depart:", queue)
print("Bus now in front:", queue[0])

# -------------------------------
# Practical 2: Airtel clients
# -------------------------------
queue = deque(["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8"])
print("\n[Queue Practical 2]")
print("Initial Queue:", queue)

served1 = queue.popleft()
served2 = queue.popleft()
print("First served:", served1)
print("Second served:", served2)

# -------------------------------
# Challenge: School lunch line
# -------------------------------
queue = deque(["S1", "S2", "S3", "S4"])
print("\n[Queue Challenge]")
print("Serving students in queue order:")
while queue:
    print("Served:", queue.popleft())

print("\n=====================================")
print("END OF EXERCISE")
print("=====================================")
