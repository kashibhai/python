marks = {
    "Kashif": 100,
    "Toseef": 56,
    "Asad": 23,
    0: "Hassan"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"kashif": 99, "toseef": 100})
# print(marks)

print(marks.get("kashif2")) # Prints None
print(marks["kashif2"]) # Returns an error