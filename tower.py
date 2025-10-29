def towers_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    towers_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    towers_of_hanoi(n - 1, auxiliary, source, destination)

print("TOWERS OF HANOI ")
n = int(input("Enter the number of disks: "))
print(f"\nSteps to move {n} disks from A to C:\n")
towers_of_hanoi(n, 'A', 'B', 'C')
