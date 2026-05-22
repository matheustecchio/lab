from set import Set
import validation as valid

def load_data(filename: str) -> list[object]:
    sets = []
    
    with open(filename, 'r') as file:
        for line in file:
            set_id, title, pieces, rrp, stock = line.split(',')
            new_set = Set(set_id, title, pieces, rrp, stock)
            sets.append(new_set)
    
    return sets


def display_sets(sets: list[object]) -> None:
    print("\nLego Sets\n" + "-" * 80)
    
    for set in sets:
        title_gap = 46 - len(set.title)
        pieces_gap = 10 - len(set.pieces)
        rrp_gap = 10 - len(set.rrp)
        
        print(
            set.set_id +    " "                 + 
            set.title +     " " * title_gap     + "\t" +
            set.pieces +    " " * pieces_gap    + 
            set.rrp +       " " * rrp_gap       + 
            set.stock
            )

def add_data(filename: str, sets: list[object]) -> None:
    set_id =    valid.read_lego_code("Set ID(Please enter a number with 5 to 7 digits): ")
    title =     valid.read_valid_lego_name("Title: ")
    pieces =    valid.read_integer("Pieces(10 to 5,000): ", 10, 5000)
    rrp =       valid.read_float("RRP(10 to 10,0000): ", 10, 10000)
    stock =     valid.read_integer  ("Stock(Max. 100): ", 0, 100)
    
    try:
        with open(filename, 'a') as file:
            for set in sets:
                if set_id == set.set_id:
                    print("ERROR: Set ID already exists.")
                    return
            
            file.write(f"{set_id},{title},{pieces},{rrp},{stock}\n") 
            sets.append(Set(set_id, title, pieces, rrp, stock))
    except:
        print("ERROR: Unable to write to the data file.\n")
        return
    else:
        print("LEGO Set added successfully.\n")

def search_by_id(sets: list[object], pattern: str) -> None:    
    searched_sets = []
    
    for set in sets:
        if set.set_id.startswith(pattern):
            searched_sets.append(set)
    if len(searched_sets) == 0:
        print("\nNo sets whose code starts with " + pattern)
    
    else:
        print("\nSets whose code starts with " + pattern + "\n")
        display_sets(searched_sets)

def main():
    while True:
        try: 
            sets = load_data('data.csv')
        except FileNotFoundError:
            print("ERROR: Data file not found.")
            exit(1)

        print("Lego Set Inventory Menu")
        print("-" * 30)
        print("1. Display Inventory")
        print("2. Add New LEGO Set")
        print("3. Search by ID")
        print("4. Placeholder")
        print("5. Placeholder")
        print("6. Placeholder")
        print("7. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_sets(sets)
        if choice == 2:
            add_data('data.csv', sets)
        if choice == 3:
            search_pattern = input("Enter a Set ID to search: ")
            search_by_id(sets, search_pattern)
        if choice == 4:
            pass
        if choice == 5:
            pass
        if choice == 6:
            pass
        if choice == 7:
            exit(0)

if __name__ == "__main__":
    main()