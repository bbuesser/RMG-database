# This file contains a dictionary of kinetics families.  The families
# set to `True` are recommended by RMG and turned on by default by setting
# kineticsFamilies = 'default' in the RMG input file. Families set to `False` 
# are not turned on by default because the family is severely lacking in data.
# These families should only be turned on with caution.

recommendedFamilies = {
'1,2-Birad_to_alkene': True,
'1,2_Insertion': True,
'1,2_shiftS': True,
'1,3_Insertion_CO2': True, 
'1,3_Insertion_ROR': True,
'1,3_Insertion_RSR': True,
'1,4_Cyclic_birad_scission': True,
'1,4_Linear_birad_scission': True,
'1+2_Cycloaddition': True,
'2+2_cycloaddition_CCO': True,
'2+2_cycloaddition_Cd': True,
'2+2_cycloaddition_CO': True,
'Birad_recombination': True,
'Cyclic_Ether_Formation': True,
'Diels_alder_addition': True,
'Disproportionation': True,
'H_Abstraction': True,
'HO2_Elimination_from_PeroxyRadical': True,
'Intra_Diels_alder': True,
'Intra_Disproportionation': True,
'intra_H_migration': True,
'intra_NO2_ONO_conversion': True,
'intra_OH_migration': True,
'Intra_R_Add_Endocyclic': True,
'Intra_R_Add_Exocyclic': True,
'intra_substitutionCS_cyclization': True,
'intra_substitutionCS_isomerization': True,
'intra_substitutionS_cyclization': True,
'intra_substitutionS_isomerization': True,
'ketoenol': True,
'Korcek_step1': False,
'Korcek_step2': False,
'lone_electron_pair_bond': True,
'Oa_R_Recombination': True,
'R_Addition_COm': True,
'R_Addition_CSm': True,
'R_Addition_MultipleBond': True,
'R_Recombination': True,
'Substitution_O': True,
'SubstitutionS': True,
}

