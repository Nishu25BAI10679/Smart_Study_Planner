print("\nSMART STUDY PLANNER\n")
subjects = {}
num_subjects = int(input("How many subjects do you want to plan for? "))
for i in range(num_subjects):
    name = input(f"\nEnter subject {i+1} name: ")
    difficulty = int(input(f"Difficulty level for {name} (1 = easy, 5 = hard): "))    
    subjects[name] = difficulty
total_hours = float(input("\nHow many hours can you study today? "))
# calculate total difficulty weight
total_difficulty = sum(subjects.values())
print("\nToday's Study Plan\n")
schedule = {}
for subject, difficulty in subjects.items():
    allocatedtime = (difficulty / total_difficulty) * total_hours
    schedule[subject] = round(allocatedtime, 2)

    print(f"{subject} → {round(allocatedtime, 2)} hrs")
# save to file
with open("study_schedule.txt", "w") as file:
    file.write("Study Plan\n\n")
    for subject, time in schedule.items():
        file.write(f"{subject} → {time} hrs\n")
print("\nSchedule saved to study_schedule.txt")