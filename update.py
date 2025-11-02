from data import language_colors

print("Fetching language color data...")
print("-----------------------")

language_colors.update_colors()

print("All fetched!")
print("-----------------------")
print("Fetching repo data...")
print("-----------------------")

from data import fetch_data

print("All repos data fetched!")
print("-----------------------")
print("Building plot...")

from analysis import build_plot

print("Plot built")
print("-----------------------")
print("All done!")
