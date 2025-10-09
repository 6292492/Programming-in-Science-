dna = 'gctagctagctagcta'
exons = [(0,3),(5,8)]
annot = list(dna.lower())
for s,e in exons:    
  for i in range(s,e):        
    annot[i] = annot[i].upper()
print(''.join(annot))
dna = 'gctagctagctagcta'
counts = {nuc: dna.upper().count(nuc) for nuc in 'ATGC'}
print(counts)
dna = 'gctagctagctagcta'
print(dna[::-1])




