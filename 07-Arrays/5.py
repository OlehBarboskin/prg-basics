# Sort the data from lowest to highest value
distances_traveled = [120, 150, 180, 90, 200, 175, 160]
# Sort the data in descending order, from highest to lowest value
daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
# Sort the data in ascending order
file_names = ["report.docx", "presentation.pptx", "data.csv", "photo.jpg", "notes.txt",
   "invoice.pdf", "resume.docx", "budget.xlsx", "meeting.mp4", "schedule.pdf"]

sorted_distances = sorted(distances_traveled)
sorted_temperatures = sorted(daily_temperatures, reverse = True)
sorted_file_names = sorted(file_names)

print("Sorted distances traveled (ascending):", sorted_distances)
print("Sorted daily temperatures (descending):", sorted_temperatures)   
print("Sorted file names (ascending):", sorted_file_names)