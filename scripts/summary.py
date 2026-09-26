import csv

# Read the observation data
with open('data/observations.csv', mode='r') as file:
    reader = csv.DictReader(file)
    dogs = list(reader)

print("===== Street Dogs of Manjari - Summary =====\n")

print(f"Total dogs recorded: {len(dogs)}\n")

# Count by Sex
males = sum(1 for dog in dogs if dog['Sex'] == 'Male')
females = sum(1 for dog in dogs if dog['Sex'] == 'Female')

print("Sex Distribution:")
print(f"  Male   : {males}")
print(f"  Female : {females}\n")

# Health summary
print("Visible Health Conditions:")
for dog in dogs:
    name = dog['Dog_Name']
    ear = dog['Ear_Cut'] or "Not recorded"
    ticks = dog['Ticks'] or "Not recorded"
    limp = dog['Limping'] or "Not recorded"
    print(f"  {name}: Ear Cut = {ear}, Ticks = {ticks}, Limping = {limp}")

print("\n===== End of Summary =====")
