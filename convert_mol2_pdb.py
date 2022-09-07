from os import mkdir, chdir, listdir, system, path
from sys import argv

out_dir = './flexicarboxi_pdb'
use_dir = argv[1]

dir_files = listdir(use_dir)
dirs = [x for x in dir_files if path.isdir(x)]

print(len(dirs), 'encontrados')

for d in dirs:
    print(d)
    chdir(d)
    dir_out = 'sulfas_' + d.split('.')[0].split('_')[1]
    print(dir_out)
    
    mol2 = listdir('.')
    mol2_files = []

    # Listamos archivos mol2 solamente
    for fi in mol2:
        fi_split = fi.split('.')
        if fi_split[1] == 'mol2':
            mol2_files.append(fi)
    print(f'Archivos {len(mol2_files)}')
    mkdir(dir_out)
    for x in mol2_files:
        system(f"babel -imol2 {x} -opdb ./{dir_out}/{x.split('.')[0]}.pdb")
    chdir('..')


