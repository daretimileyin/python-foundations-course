"""Example 03 – Importing from your own package (see the my_package/ folder)."""
from my_package import text_tools
from my_package.geometry import circle_area, rectangle_area

print(f"Circle area (r=3): {circle_area(3):.2f}")
print("Rectangle area (4x5):", rectangle_area(4, 5))
print(text_tools.shout("modules are great"))
print("Words:", text_tools.word_count("I can split code across files"))
print("\ntext_tools.__name__ is", text_tools.__name__)
print("This file's __name__ is", __name__)
