import glob

csv_files = glob.glob("./Question1/Dataset/*.csv")
count = len(csv_files)

print(f"CSV File Count: {count} files")
