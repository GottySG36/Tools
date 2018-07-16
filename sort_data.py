import os, sys

file = sys.argv[1]
outfile = file + '_sort'

with open(file,'r') as data_in:
    with open(outfile, 'w') as data_out:
        nb = 0
        for line in data_in:
            if line [0] == '>':
                nb = 0
                header = line
            if line[0] != '>':
                nb += 1
                if nb == 1:
                    line1 == line
                elif nb == 2:
                    data_out.write(header)
                    data_out.write(line1)
                    data_out.write(line)
                elif nb > 2:
                    data_out.write(line)

data_in.close()
data_out.close()
                
