import re
import itertools as it

from Best_K_Mer import Best_K_Mer

def main():
    # Pull in file data
    input_1 = open("input_3.txt", "r")
    k = int(input_1.readline())
    dna_string = input_1.readline()
    dna_list = re.split("\s", dna_string)

    #Have k-mer and list of DNA, now need to iterate through all possible patterns of length k
    letters = ["A", "C", "G", "T"]
    best_k_mer = Best_K_Mer("", -1)

    for k_mer in it.product(letters, repeat=k):
        distance = d(k_mer, dna_list)
        if distance < best_k_mer.distance or best_k_mer.distance == -1:
            best_k_mer = Best_K_Mer(k_mer, distance)

    print(best_k_mer.dna)

def d(k_mer, dna):
    total_distance = 0
    for dna_portion in dna:
        current_lowest_distance = -1
        current_distance = 0
        for i in range(len(dna_portion) - len(k_mer) + 1):
            for j in range(len(k_mer)):
                if (k_mer[j] != dna_portion[i + j]):
                    current_distance += 1

        if current_distance < current_lowest_distance or current_lowest_distance == -1:
            current_lowest_distance = current_distance

        total_distance += current_lowest_distance
    return total_distance


if __name__ == "__main__":
    main()