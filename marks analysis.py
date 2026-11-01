import numpy as np

# 1. Create a marks matrix using default_rng
rng = np.random.default_rng(seed=42)
marks = rng.integers(0, 101, size=(10, 5))

print("=== 1. MARKS MATRIX (10 Students x 5 Subjects) ===")
print(marks)
print("\n" + "="*50 + "\n")

# 2. Calculate student performance (Total marks and Percentage)
total_marks = np.sum(marks, axis=1)
percentage = (total_marks / 500) * 100

print("=== 2. STUDENT PERFORMANCE ===")
for i in range(10):
    print(f"Student {i+1}: Total Marks = {total_marks[i]}/500 | Percentage = {percentage[i]:.2f}%")
print("\n" + "="*50 + "\n")

# 3. Analyze subject performance (Average marks and Standard Deviation)
avg_subject_marks = np.mean(marks, axis=0)
std_subject_marks = np.std(marks, axis=0)

print("=== 3. SUBJECT PERFORMANCE ANALYSIS ===")
for j in range(5):
    print(f"Subject {j+1}: Average Marks = {avg_subject_marks[j]:.2f} | Standard Deviation = {std_subject_marks[j]:.2f}")
print("\n" + "="*50 + "\n")

# 4. Find subject toppers using argmax
highest_marks = np.max(marks, axis=0)
topper_indices = np.argmax(marks, axis=0)

print("=== 4. SUBJECT TOPPERS ===")
for j in range(5):
    print(f"Subject {j+1} Topper: Student {topper_indices[j]+1} with {highest_marks[j]} marks")
print("\n" + "="*50 + "\n")

# 5. Identify pass and fail students using a Boolean mask
passing_threshold = 40
pass_mask = marks >= passing_threshold
passed_all_subjects = np.all(pass_mask, axis=1)

passed_students = np.where(passed_all_subjects)[0]
failed_students = np.where(~passed_all_subjects)[0]

print("=== 5. PASS / FAIL ANALYSIS (Passing criteria: >= 40 in all subjects) ===")
print(f"Passed Students (Indices): {[s+1 for s in passed_students]}")
print(f"Failed/At-Risk Students (Indices): {[s+1 for s in failed_students]}")