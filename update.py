from data import analysis, language_colors, repositories_data

print("Fetching language color data...")
print()

language_colors.update_colors()

print("All fetched!")
print()

print("Fetching repo data...")
print()

repositories_data.update_repositories_data()

print("All repos data fetched!")
print()

print("Building plot...")
print()

analysis.update_plot()

print("Plot built")
print()

print("All done!")
