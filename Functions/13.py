subject_marks = [('Database', 68), ('Computing', 70), 
('Networking', 86)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(subject_marks)
