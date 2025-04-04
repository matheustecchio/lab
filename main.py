from set import Set

def load_data(filename):
    sets = []
    
    with open(filename, 'r') as file:
        for line in file:
            set_id, title, pieces, rrp, stock = line.split(',')
            new_set = Set(set_id, title, pieces, rrp, stock)
            sets.append(new_set)
    
    return sets

def main():
    pass

if __name__ == "__main__":
    main()