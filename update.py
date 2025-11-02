from data import language_colors, repositories_data

print("Fetching language color data...")

language_colors.update_colors()

print("All fetched!")
print()

print("Fetching repo data...")

repositories_data.update_repositories_data()

print("All repos data fetched!")
print()

print("Building plot...")

from analysis import build_plot

print("Plot built")
print()

print("All done!")
