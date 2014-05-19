#!/usr/bin/env python
# encoding: utf-8

name = "1,3_Insertion_CO2/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["CO2", "RR'"], products=["R_(CO2)_R'"], ownReverse=False)

reverse = "1,2_Elimination_CO2"

recipe(actions=[
    ['BREAK_BOND', '*3', 'S', '*4'],
    ['CHANGE_BOND', '*1', '-1', '*2'],
    ['FORM_BOND', '*1', 'S', '*3'],
    ['FORM_BOND', '*2', 'S', '*4'],
])

entry(
    index = 1,
    label = "CO2",
    group = "OR{CO2_Od, CO2_Cdd}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "RR'",
    group = "OR{R_H, R_R'}",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "CO2_Od",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *2 Cdd U0 {2,D} {3,D}
2 *1 Od  U0 {1,D}
3    Od  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "CO2_Cdd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *1 Cdd U0 {2,D} {3,D}
2 *2 Od  U0 {1,D}
3    Od  U0 {1,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "R_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 {H,Cs,Cd,Cb,Sis,Sid,N} U0 {2,S}
2 *4 H                      U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "H2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 H U0 {2,S}
2 *4 H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "Cb_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cb       U0 {2,B} {3,S}
2    {Cb,Cbf} U0 {1,B}
3 *4 H        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "Cd_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U0 {2,D} {3,S} {4,S}
2    Cd U0 {1,D}
3 *4 H  U0 {1,S}
4    R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "Cd_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U0 {2,D} {3,S} {4,S}
2    Cd U0 {1,D}
3 *4 H  U0 {1,S}
4    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 10,
    label = "Cd_sec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd  U0 {2,D} {3,S} {4,S}
2    Cd  U0 {1,D}
3 *4 H   U0 {1,S}
4    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "Cd/H/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U0 {2,D} {3,S} {4,S}
2    Cd U0 {1,D}
3 *4 H  U0 {1,S}
4    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 12,
    label = "Cd/H/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd U0 {2,D} {3,S} {4,S}
2    Cd U0 {1,D}
3 *4 H  U0 {1,S}
4    Os U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "Cd/H/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cd            U0 {2,D} {3,S} {4,S}
2    Cd            U0 {1,D}
3 *4 H             U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "Cs_H",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  U0 {1,S}
3    R  U0 {1,S}
4    R  U0 {1,S}
5    R  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "C_methane",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "C_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs  U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H   U0 {1,S}
3    H   U0 {1,S}
4    H   U0 {1,S}
5    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "C_pri/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "C_pri/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    Os U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "C_pri/De",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             U0 {1,S}
3    H             U0 {1,S}
4    H             U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "C_sec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs  U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H   U0 {1,S}
3    H   U0 {1,S}
4    R!H U0 {1,S}
5    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "C/H2/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  U0 {1,S}
3    H  U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "C/H2/NonDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs     U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H      U0 {1,S}
3    H      U0 {1,S}
4    O      U0 {1,S}
5    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "C/H2/CsO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  U0 {1,S}
3    H  U0 {1,S}
4    O  U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "C/H2/O2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  U0 {1,S}
3    H  U0 {1,S}
4    O  U0 {1,S}
5    O  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "C/H2/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             U0 {1,S}
3    H             U0 {1,S}
4    {Cd,Ct,CO,Cb} U0 {1,S}
5    {Cs,O}        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 26,
    label = "C/H2/OneDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             U0 {1,S}
3    H             U0 {1,S}
4    {Cd,Ct,CO,Cb} U0 {1,S}
5    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 27,
    label = "C/H2/OneDeO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             U0 {1,S}
3    H             U0 {1,S}
4    {Cd,Ct,CO,Cb} U0 {1,S}
5    O             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 28,
    label = "C/H2/TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             U0 {1,S}
3    H             U0 {1,S}
4    {Cd,Ct,CO,Cb} U0 {1,S}
5    {Cd,Ct,CO,Cb} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 29,
    label = "C_ter",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs  U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H   U0 {1,S}
3    R!H U0 {1,S}
4    R!H U0 {1,S}
5    R!H U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 30,
    label = "C/H/NonDeC",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs     U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H      U0 {1,S}
3    {Cs,O} U0 {1,S}
4    {Cs,O} U0 {1,S}
5    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 31,
    label = "C/H/Cs3",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H  U0 {1,S}
3    Cs U0 {1,S}
4    Cs U0 {1,S}
5    Cs U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 32,
    label = "C/H/NDMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs     U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H      U0 {1,S}
3    O      U0 {1,S}
4    {Cs,O} U0 {1,S}
5    {Cs,O} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 33,
    label = "C/H/OneDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cs,O}        U0 {1,S}
5    {Cs,O}        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 34,
    label = "C/H/Cs2",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    Cs            U0 {1,S}
5    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 35,
    label = "C/H/ODMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    O             U0 {1,S}
5    {Cs,O}        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 36,
    label = "C/H/TwoDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    {Cs,O}        U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 37,
    label = "C/H/Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    Cs            U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 38,
    label = "C/H/TDMustO",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    O             U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 39,
    label = "C/H/ThreeDe",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs            U0 {2,S} {3,S} {4,S} {5,S}
2 *4 H             U0 {1,S}
3    {Cd,Ct,Cb,CO} U0 {1,S}
4    {Cd,Ct,Cb,CO} U0 {1,S}
5    {Cd,Ct,Cb,CO} U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 40,
    label = "R_R'",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 {Cs,Sis,N}           U0 {2,S} {3,S} {4,S} {5,S}
2 *4 {Cs,Cd,Cb,Sis,Sid,N} U0 {1,S}
3    H                    U0 {1,S}
4    H                    U0 {1,S}
5    H                    U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 41,
    label = "Cs_Cs",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 42,
    label = "C_methyl_C_methyl",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs U0 {1,S} {6,S} {7,S} {8,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
6    H  U0 {2,S}
7    H  U0 {2,S}
8    H  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 43,
    label = "C_methyl_C_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs U0 {1,S} {6,S} {7,S} {8,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
6    H  U0 {2,S}
7    H  U0 {2,S}
8    C  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 44,
    label = "C_methyl_C_sec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs U0 {1,S} {6,S} {7,S} {8,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
6    H  U0 {2,S}
7    C  U0 {2,S}
8    C  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 45,
    label = "C_methyl_C_ter",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cs U0 {1,S} {6,S} {7,S} {8,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
6    C  U0 {2,S}
7    C  U0 {2,S}
8    C  U0 {2,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 46,
    label = "Cs_Cd",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cd U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 47,
    label = "C_methyl_Cd_pri",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cd U0 {1,S} {6,S} {7,D}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
6    H  U0 {2,S}
7    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 48,
    label = "C_methyl_Cd_sec",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cd U0 {1,S} {6,S} {7,D}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
6    C  U0 {2,S}
7    C  U0 {2,D}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 49,
    label = "Cs_Cb",
    multiplicity = [1, 2, 3, 4, 5],
    group = 
"""
1 *3 Cs U0 {2,S} {3,S} {4,S} {5,S}
2 *4 Cb U0 {1,S}
3    H  U0 {1,S}
4    H  U0 {1,S}
5    H  U0 {1,S}
""",
    kinetics = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: CO2
    L2: CO2_Od
    L2: CO2_Cdd
L1: RR'
    L2: R_H
        L3: H2
        L3: Cb_H
        L3: Cd_H
            L4: Cd_pri
            L4: Cd_sec
                L5: Cd/H/NonDeC
                L5: Cd/H/NonDeO
                L5: Cd/H/OneDe
        L3: Cs_H
            L4: C_methane
            L4: C_pri
                L5: C_pri/NonDeC
                L5: C_pri/NonDeO
                L5: C_pri/De
            L4: C_sec
                L5: C/H2/NonDeC
                L5: C/H2/NonDeO
                    L6: C/H2/CsO
                    L6: C/H2/O2
                L5: C/H2/OneDe
                    L6: C/H2/OneDeC
                    L6: C/H2/OneDeO
                L5: C/H2/TwoDe
            L4: C_ter
                L5: C/H/NonDeC
                    L6: C/H/Cs3
                    L6: C/H/NDMustO
                L5: C/H/OneDe
                    L6: C/H/Cs2
                    L6: C/H/ODMustO
                L5: C/H/TwoDe
                    L6: C/H/Cs
                    L6: C/H/TDMustO
                L5: C/H/ThreeDe
    L2: R_R'
        L3: Cs_Cs
            L4: C_methyl_C_methyl
            L4: C_methyl_C_pri
            L4: C_methyl_C_sec
            L4: C_methyl_C_ter
        L3: Cs_Cd
            L4: C_methyl_Cd_pri
            L4: C_methyl_Cd_sec
        L3: Cs_Cb
"""
)

