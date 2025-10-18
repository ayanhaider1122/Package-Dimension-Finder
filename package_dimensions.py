# package_dimensions.py
length = float(input("Enter item length (cm): "))
width = float(input("Enter item width (cm): "))
height = float(input("Enter item height (cm): "))

package_volume = length * width * height
print(f"Package dimensions: {length} x {width} x {height} cm")
print(f"Package volume: {package_volume} cubic cm")
