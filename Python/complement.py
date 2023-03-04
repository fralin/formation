def seq_comp(seq: list) -> list:
    list_comp = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return [list_comp[base] for base in seq]

if __name__ == "__main__":
    import sys
    
    print(sys.argv)
    if len(sys.argv) == 1:
        print("Nombre d'argument insuffisant")
        sys.exit()
    seq = []
    for base in sys.argv[1:]:
        if base in "ATCG":
            seq.append(base)
        else:
            print("Erreur de paramètre")
            sys.exit()
            
    print(seq)
    print (seq_comp(seq))
           