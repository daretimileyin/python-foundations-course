total_seconds = int(input("Number of seconds: "))

hours = total_seconds // 3600
remaining = total_seconds % 3600
minutes = remaining // 60
seconds = remaining % 60

print(f"{total_seconds} seconds is {hours} hour(s), {minutes} minute(s) and {seconds} second(s).")
print(f"Digital clock: {hours:02d}:{minutes:02d}:{seconds:02d}")
