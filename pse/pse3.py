strand1 = "GAGCCTACTAACGGGAT" 
strand2 = "CATCGTAATGACGGCCT"

def hamming_distance(strand1, strand2):
    if strand1 is None or strand2 is None:
        raise ValueError("Inputs must not be empty")
    if len(strand1) == 0 or len(strand2) == 0:
        raise ValueError("Inputs must be in same size")
        
    diff = 0   
    for i , j in zip(strand1, strand2): diff += 1 if i != j else 0
    return diff


# def hamming_distance(strand1, strand2):
#     count = 0
#     for i in range(len(strand1)):
#         if strand1[i] != strand2[i]:
#             count += 1
#     return count



print(hamming_distance(strand1, strand2))


#Tests

def test_hamming_distance():
    # ^rename with meaningful test name
    # and complete test implementation below
    
    # arrange
    strand_1 = "GAGCCTACTAACGGGAT"
    strand_2 = "CATCGTAATGACGGCCT"
    # act
    result = hamming_distance(strand_1, strand_2)
    # assert
    assert result == 7
    

def test_hamming_distance_input_validate():
    # ^rename with meaningful test name
    # and complete test implementation below
    
    # arrange
    strand_1 = "GAgCCTACTAACGGGAT"
    strand_2 = "CATCGTAATGACGGCcT"
    # act
    result = hamming_distance(strand_1, strand_2)
    # assert
    assert len(strand_1) == len(strand_2)
    assert result == 7