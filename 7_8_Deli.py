sandwich_orders = ['pastrami', 'chicken', 'pastrami', 'beef', 'pastrami', 'veggie']
finished_sandwiches = []
for sandwich in sandwich_orders:
    if sandwich == 'pastrami':
        print("Sorry, we are out of pastrami.")
        continue
    print("I made your " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)
print("\nAll sandwiches have been made:")
for sandwich in finished_sandwiches:
    print("- " + sandwich)
