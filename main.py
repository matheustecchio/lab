from set import Set

def load_data(filename):
    sets = []
    
    with open(filename, 'r') as file:
        for line in file:
            set_id, title, pieces, rrp, stock = line.split(',')
            new_set = Set(set_id, title, pieces, rrp, stock)
            sets.append(new_set)
    
    return sets

def display_data(data):
    print("Lego Sets\n" + "-" * 80)
    
    
    
    for set in data:
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

def main():
    sets = load_data('data.csv')
    display_data(sets)

if __name__ == "__main__":
    main()