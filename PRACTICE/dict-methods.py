marks = {"Rohan": 85, 
         "Sohan": 90, 
         "Mohan": 78, 
         "Gita": 92, 
         "Raj": 88}
print (marks.keys())  # Output: ['Rohan', 'Sohan', 'Mohan', 'Gita', 'Raj']
print (marks.values())  # Output: [85, 90, 78, 92, 88]
print (marks.items())  # Output: [('Rohan', 85), ('Sohan', 90), ('Mohan', 78), ('Gita', 92), ('Raj', 88)]
marks.update({"Rohan": 95, "Sohan": 92})
print (marks)  # Output: {'Rohan': 95, 'Sohan': 92, 'Mohan': 78, 'Gita': 92, 'Raj': 88}

print (marks.get("Mohan2"))  # Output: none
print (marks["Mohan2"])  # Output: KeyError: 'Mohan2' 