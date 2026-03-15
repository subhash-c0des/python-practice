tasks = []

while True:
    task = input("Enter a task (or 'quit'): ")
    
    if task == "quit":
        break
        
    tasks.append(task)

print("\nYour Tasks:")
for t in tasks:
    print("-", t)