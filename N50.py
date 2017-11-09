print 'Python and Biopython needed for running this script!'

print "Script for calculating N50 of assembly"

fasta = raw_input('Enter your fasta/fa name: ')



# N50 calculation

BaseSum,Length= 0,[]

ValueSum,N50 = 0,0

no_c,no_g,no_a,no_t,no_n = 0,0,0,0,0



from Bio import SeqIO

for record in SeqIO.parse(open(fasta), "fasta"):

   BaseSum += len(record.seq)

   Length.append(len(record.seq))

   seq =record.seq.lower()

   no_c+=seq.count('c')

   no_g+=seq.count('g')

   no_a+=seq.count('a')

   no_t+=seq.count('t')

   no_n+=seq.count('n')



#N50 calcuation

N50_pos = BaseSum / 2.0    

Length.sort()  

Length.reverse()    

for value in Length:

   ValueSum += value

   if N50_pos <= ValueSum:

       N50 = value

       break  

print 'Sequences NO.:'+'t'+str(len(Length))

print 'Sequences Min.:'+'t'+str(min(Length))

print 'Sequences Max.:'+'t'+str(max(Length))

print 'N50: ' + str(N50)