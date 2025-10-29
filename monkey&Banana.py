
monkey_pos = "A"
box_pos = "B"
banana_pos = "C"
monkey_on_box = False
has_banana = False

print("Initial State:")
print(f"Monkey at: {monkey_pos}, Box at: {box_pos}, Banana at: {banana_pos}\n")

# Step 1: Monkey moves to the box
print("Step 1: Monkey moves to the box.")
monkey_pos = box_pos
print(f"Monkey at: {monkey_pos}, Box at: {box_pos}\n")

# Step 2: Monkey pushes the box under the banana
print("Step 2: Monkey pushes the box under the banana.")
box_pos = banana_pos
monkey_pos = banana_pos
print(f"Monkey at: {monkey_pos}, Box at: {box_pos}\n")

# Step 3: Monkey climbs on the box
print("Step 3: Monkey climbs on the box.")
monkey_on_box = True

# Step 4: Monkey grabs the banana
print("Step 4: Monkey grabs the banana.")
has_banana = True

# Final State
print("\nFinal State:")
print(f"Monkey at: {monkey_pos}, Box at: {box_pos}")
print(f"Monkey on box: {monkey_on_box}, Has banana: {has_banana}")
print("\n✅ Monkey successfully got the banana!")
