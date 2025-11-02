from data import analysis, language_colors, repositories_data

print("Fetching language color data...")

language_colors.update_colors()

print("All fetched!")
print()

print("Fetching repo data...")

repositories_data.update_repositories_data()

print("All repos data fetched!")
print()

print("Building plot...")

analysis.update_plot()

print("Plot built")
print()

print("All done!")
