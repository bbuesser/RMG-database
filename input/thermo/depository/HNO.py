#!/usr/bin/env python
# encoding: utf-8

name = "thermo_DFT_CCSDTF12_BAC"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = 19,
    label = "HOOH",
    molecule = """
1 O 0 {2,S} {3,S}
2 O 0 {1,S} {4,S}
3 H 0 {1,S}
4 H 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([9.91,10.83,11.68,12.44,13.71,14.69,16.28],'cal/(mol*K)'),
        H298 = (-32.58,'kcal/mol'),
        S298 = (55.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 318,
    label = "HONO",
    molecule =         """
        1 O 0 2 {2,D}
        2 N 0 1 {1,D} {3,S}
        3 O 0 2 {2,S} {4,S}
        4 H 0 0 {3,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.28,12.62,13.73,14.62,15.99,16.93,18.12],'cal/(mol*K)'),
        H298 = (-18.17,'kcal/mol'),
        S298 = (59.89,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 319,
    label = "NO2OH",
    molecule =         """
        1 O 0 3 {3,S}
        2 O 0 2 {3,D}
        3 N 0 0 {1,S} {2,D} {4,S}
        4 O 0 2 {3,S} {5,S}
        5 H 0 0 {4,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.80,15.22,17.09,18.44,20.42,21.72,23.22],'cal/(mol*K)'),
        H298 = (-31.75,'kcal/mol'),
        S298 = (63.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

#entry(
#    index = 323,
#    label = "NH3",
#    molecule =         """
#        1 H 0 0 {3,S}
#        2 H 0 0 {3,S}
#        3 N 0 1 {1,S} {2,S} {4,S}
#        4 H 0 0 {3,S}
#        """,
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([8.49,9.05,9.74,10.48,11.92,13.16,15.50],'cal/(mol*K)'),
#        H298 = (-10.69,'kcal/mol'),
#        S298 = (45.99,'cal/(mol*K)'),
#    ),
#    shortDesc = u"""""",
#    longDesc = 
#u"""
# level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
#""",
#    history = [
#        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
#    ],
#)

entry(
    index = 324,
    label = "NH2OH",
    molecule =         """
        1 H 0 0 {3,S}
        2 H 0 0 {3,S}
        3 N 0 1 {1,S} {2,S} {4,S}
        4 O 0 2 {3,S} {5,S}
        5 H 0 0 {4,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([10.56,12.28,13.96,15.47,17.76,19.35,21.59],'cal/(mol*K)'),
        H298 = (-9.68,'kcal/mol'),
        S298 = (56.05,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 330,
    label = "HNNH",
    molecule =         """
        1 H 0 0 {2,S}
        2 N 0 1 {1,S} {3,D}
        3 N 0 1 {2,D} {4,S}
        4 H 0 0 {3,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([8.42,9.19,10.14,11.15,12.92,14.32,16.61],'cal/(mol*K)'),
        H298 = (47.63,'kcal/mol'),
        S298 = (52.10,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 331,
    label = "NH2NO2",
    molecule =         """
        1 N 0 1 {2,S} {3,S} {4,S}
        2 H 0 0 {1,S}
        3 H 0 0 {1,S}
        4 N 0 0 {1,S} {5,D} {6,S}
        5 O 0 2 {4,D}
        6 O 0 3 {4,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.00,15.71,17.80,19.38,21.82,23.55,25.95],'cal/(mol*K)'),
        H298 = (0.45,'kcal/mol'),
        S298 = (63.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, cosine rotor fit
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 333,
    label = "NH2NH2",
    molecule =         """
        1 N 0 1 {2,S} {3,S} {4,S}
        2 H 0 0 {1,S}
        3 H 0 0 {1,S}
        4 N 0 1 {1,S} {5,S} {6,S}
        5 H 0 0 {4,S}
        6 H 0 0 {4,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.55,13.62,15.48,17.08,19.74,21.81,25.17],'cal/(mol*K)'),
        H298 = (23.35,'kcal/mol'),
        S298 = (56.84,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

#entry(
#    index = 334,
#    label = "N2O",
#    molecule =         """
#        1 N 0 2 {2,D}
#        2 N 0 0 {1,D} {3,D}
#        3 O 0 2 {2,D}
#        """,
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([9.20,10.11,10.88,11.50,12.44,13.08,13.90],'cal/(mol*K)'),
#        H298 = (19.74,'kcal/mol'),
#        S298 = (52.59,'cal/(mol*K)'),
#    ),
#    shortDesc = u"""""",
#    longDesc = 
#u"""
# level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
#""",
#    history = [
#        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
#    ],
#)

entry(
    index = 335,
    label = "NO2NO",
    molecule =         """
        1 N 0 0 {2,D} {3,S} {4,S}
        2 O 0 2 {1,D}
        3 O 0 3 {1,S}
        4 N 0 1 {1,S} {5,D}
        5 O 0 2 {4,D}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.99,18.58,19.80,20.79,22.23,23.10,23.95],'cal/(mol*K)'),
        H298 = (19.90,'kcal/mol'),
        S298 = (71.97,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 336,
    label = "NO2NO2",
    molecule =         """
        1 N 0 0 {2,D} {3,S} {4,S}
        2 O 0 2 {1,D}
        3 O 0 3 {1,S}
        4 N 0 0 {1,S} {5,D} {6,S}
        5 O 0 2 {4,D}
        6 O 0 3 {4,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.78,21.47,23.46,24.94,27.10,28.46,29.85],'cal/(mol*K)'),
        H298 = (2.35,'kcal/mol'),
        S298 = (73.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 337,
    label = "NO2ONO2",
    molecule =         """
        1 N 0 0 {2,D} {3,S} {4,S}
        2 O 0 2 {1,D}
        3 O 0 3 {1,S}
        4 O 0 2 {1,S} {5,S}
        5 N 0 0 {4,S} {6,D} {7,S}
        6 O 0 2 {5,D}
        7 O 0 3 {5,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.31,23.22,25.61,27.57,30.39,32.14,33.98],'cal/(mol*K)'),
        H298 = (3.90,'kcal/mol'),
        S298 = (84.17,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

#entry(
#    index = 339,
#    label = "HNNN",
#    molecule =         """
#        1 H 0 0 {2,S}
#        2 N 0 1 {1,S} {3,D}
#        3 N 0 0 {2,D} {4,D}
#        4 N 0 2 {3,D}
#        """,
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([10.61,11.83,12.83,13.69,15.07,16.08,17.59],'cal/(mol*K)'),
#        H298 = (69.78,'kcal/mol'),
#        S298 = (57.18,'cal/(mol*K)'),
#    ),
#    shortDesc = u"""""",
#    longDesc = 
#u"""
# level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
#""",
#    history = [
#        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
#    ],
#)

entry(
    index = 340,
    label = "NO2ONO",
    molecule =         """
        1 O 0 2 {3,D}
        2 O 0 3 {3,S}
        3 N 0 0 {1,D} {2,S} {4,S}
        4 O 0 2 {3,S} {5,S}
        5 N 0 1 {4,S} {6,D}
        6 O 0 2 {5,D}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.70,21.28,23.11,24.55,26.68,28.02,29.42],'cal/(mol*K)'),
        H298 = (10.61,'kcal/mol'),
        S298 = (76.44,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)
#
#entry(
#    index = 343,
#    label = "NNH2",
#    molecule =         """
#        1 N 0 0 {2,S} {3,S} {4,D}
#        2 H 0 0 {1,S}
#        3 H 0 0 {1,S}
#        4 N 0 2 {1,D}
#        """,
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([8.61,9.45,10.46,11.48,13.24,14.63,16.86],'cal/(mol*K)'),
#        H298 = (71.66,'kcal/mol'),
#        S298 = (52.09,'cal/(mol*K)'),
#    ),
#    shortDesc = u"""""",
#    longDesc = 
#u"""
# level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
#""",
#    history = [
#        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
#    ],
#)

#entry(
#    index = 347,
#    label = "HNO",
#    molecule =         """
#        1 H 0 0 {2,S}
#        2 N 0 1 {1,S} {3,D}
#        3 O 0 2 {2,D}
#        """,
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([8.09,8.42,8.87,9.37,10.34,11.11,12.35],'cal/(mol*K)'),
#        H298 = (25.34,'kcal/mol'),
#        S298 = (52.71,'cal/(mol*K)'),
#    ),
#    shortDesc = u"""""",
#    longDesc = 
#u"""
# level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
#""",
#    history = [
#        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
#    ],
#)

entry(
    index = 354,
    label = "ONNO_cis",
    molecule = """
1 O 0 2 {2,D}
2 N 0 1 {1,D} {3,S}
3 N 0 1 {2,S} {4,D}
4 O 0 2 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([13.35,15.28,16.71,17.60,18.54,18.94,18.86],'cal/(mol*K)'),
        H298 = (42.50,'kcal/mol'),
        S298 = (63.86,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 357,
    label = "ONOONO",
    molecule = """
1 O 0 2 {2,D}
2 N 0 1 {1,D} {3,S}
3 O 0 2 {2,S} {4,S}
4 O 0 2 {3,S} {5,S}
5 N 0 1 {4,S} {6,D}
6 O 0 2 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.09,25.22,26.70,27.89,29.59,30.58,31.32],'cal/(mol*K)'),
        H298 = (31.51,'kcal/mol'),
        S298 = (76.59,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, no O-O rotor
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

#entry(
#    index = 358,
#    label = "HNO2",
#    molecule = """
#1 H 0 0 {2,S}
#2 N 0 0 {1,S} {3,D} {4,S}
#3 O 0 2 {2,D}
#4 O 0 3 {2,S}
#""",
#    thermo = ThermoData(
#        Tdata = ([300,400,500,600,800,1000,1500],'K'),
#        Cpdata = ([9.27,10.47,11.71,12.86,14.66,15.91,17.69],'cal/(mol*K)'),
#        H298 = (-10.40,'kcal/mol'),
#        S298 = (58.29,'cal/(mol*K)'),
#    ),
#    shortDesc = u"""""",
#    longDesc = 
#u"""
# level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
#""",
#    history = [
#        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
#    ],
#)

entry(
    index = 360,
    label = "ONOOH",
    molecule = """
1 O 0 2 {2,D}
2 N 0 1 {1,D} {3,S}
3 O 0 2 {2,S} {4,S}
4 O 0 2 {3,S} {5,S}
5 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.64,17.29,18.52,19.53,21.04,22.05,23.23],'cal/(mol*K)'),
        H298 = (-2.60,'kcal/mol'),
        S298 = (69.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 361,
    label = "ONONO",
    molecule = """
1 O 0 2 {2,D}
2 N 0 1 {1,D} {3,S}
3 O 0 2 {2,S} {4,S}
4 N 0 1 {3,S} {5,D}
5 O 0 2 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.59,21.61,23.42,24.36,25.35,25.62,24.92],'cal/(mol*K)'),
        H298 = (21.77,'kcal/mol'),
        S298 = (69.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 363,
    label = "NO2OOH",
    molecule = """
1 N 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 O 0 3 {1,S}
4 O 0 2 {1,S} {5,S}
5 O 0 2 {4,S} {6,S}
6 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.02,20.77,22.60,23.99,26.02,27.29,28.58],'cal/(mol*K)'),
        H298 = (-12.10,'kcal/mol'),
        S298 = (72.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 369,
    label = "NH2OOH",
    molecule = """
1 N 0 1 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 O 0 2 {1,S} {5,S}
5 O 0 2 {4,S} {6,S}
6 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.35,16.67,18.52,20.04,22.44,24.16,26.56],'cal/(mol*K)'),
        H298 = (3.07,'kcal/mol'),
        S298 = (64.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, NH2 rotor rigid scan
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 373,
    label = "HONNOH",
    molecule = """
1 H 0 0 {2,S}
2 O 0 2 {1,S} {3,S}
3 N 0 1 {2,S} {4,D}
4 N 0 1 {3,D} {5,S}
5 O 0 2 {4,S} {6,S}
6 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.43,20.17,21.99,23.31,25.26,26.49,27.84],'cal/(mol*K)'),
        H298 = (5.23,'kcal/mol'),
        S298 = (65.75,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 374,
    label = "HNOHOH",
    molecule = """
1 H 0 0 {2,S}
2 N 0 1 {1,S} {3,S} {5,S}
3 O 0 2 {2,S} {4,S}
4 H 0 0 {3,S}
5 O 0 2 {2,S} {6,S}
6 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.47,18.11,20.08,21.46,23.46,24.81,26.59],'cal/(mol*K)'),
        H298 = (-21.90,'kcal/mol'),
        S298 = (63.43,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 375,
    label = "NH2OH",
    molecule = """
1 N 0 1 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 O 0 2 {1,S} {5,S}
5 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.11,12.98,14.69,16.10,18.14,19.57,21.56],'cal/(mol*K)'),
        H298 = (-9.63,'kcal/mol'),
        S298 = (56.30,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 382,
    label = "NO2ONO2",
    molecule = """
1 N 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 O 0 3 {1,S}
4 O 0 2 {1,S} {5,S}
5 N 0 0 {4,S} {6,D} {7,S}
6 O 0 2 {5,D}
7 O 0 3 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.12,24.64,26.98,28.79,31.39,32.97,34.41],'cal/(mol*K)'),
        H298 = (3.84,'kcal/mol'),
        S298 = (83.50,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 386,
    label = "HNNOH",
    molecule = """
1 H 0 0 {2,S}
2 N 0 1 {1,S} {3,D}
3 N 0 1 {2,D} {4,S}
4 O 0 2 {3,S} {5,S}
5 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.18,14.11,15.77,17.11,19.17,20.62,22.55],'cal/(mol*K)'),
        H298 = (19.35,'kcal/mol'),
        S298 = (61.24,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 389,
    label = "ONOONO2",
    molecule = """
1 O 0 2 {2,D}
2 N 0 1 {1,D} {3,S}
3 O 0 2 {2,S} {4,S}
4 O 0 2 {3,S} {5,S}
5 N 0 0 {4,S} {6,D} {7,S}
6 O 0 2 {5,D}
7 O 0 3 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.47,27.37,29.74,31.63,34.26,35.71,36.57],'cal/(mol*K)'),
        H298 = (19.99,'kcal/mol'),
        S298 = (84.30,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVDZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 392,
    label = "NO2OONO2",
    molecule = """
1 N 0 0 {2,D} {3,S} {4,S}
2 O 0 2 {1,D}
3 O 0 3 {1,S}
4 O 0 2 {1,S} {5,S}
5 O 0 2 {4,S} {6,S}
6 N 0 0 {5,S} {7,D} {8,S}
7 O 0 2 {6,D}
8 O 0 3 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.13,29.07,32.28,34.86,38.46,40.51,41.95],'cal/(mol*K)'),
        H298 = (9.17,'kcal/mol'),
        S298 = (85.26,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVDZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 398,
    label = "HNNNH2",
    molecule = """
1 N 0 1 {2,S} {4,S} {5,S}
2 N 0 1 {1,S} {3,D}
3 N 0 1 {2,D} {6,S}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 H 0 0 {3,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.92,14.14,16.00,17.52,20.01,21.88,24.80],'cal/(mol*K)'),
        H298 = (54.00,'kcal/mol'),
        S298 = (59.90,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC, cosine rotor fit
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 431,
    label = "NH2NO",
    molecule = """
1  N 0 1 {2,S} {3,S} {4,S}
2  H 0 0 {1,S}
3  H 0 0 {1,S}
4  N 0 1 {1,S} {5,D}
5  O 0 2 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.88,13.80,15.49,16.89,19.03,20.56,22.69],'cal/(mol*K)'),
        H298 = (18.82,'kcal/mol'),
        S298 = (59.74,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 433,
    label = "NH2NHNO",
    molecule = """
1  N 0 1 {2,S} {3,S} {4,S}
2  H 0 1 {1,S}
3  H 0 1 {1,S}
4  N 0 1 {1,S} {5,S} {6,D}
5  H 0 1 {4,S}
6  O 0 2 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.23,19.81,22.07,24.04,27.17,29.40,32.64],'cal/(mol*K)'),
        H298 = (42.28,'kcal/mol'),
        S298 = (69.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 437,
    label = "NH2ONO",
    molecule = """
1 N 0 1 {2,S} {4,S} {5,S}
2 O 0 2 {1,S} {3,S}
3 N 0 1 {2,S} {6,D}
4 H 0 0 {1,S}
5 H 0 0 {1,S}
6 O 0 2 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.25,20.03,21.33,22.45,24.25,25.57,27.53],'cal/(mol*K)'),
        H298 = (24.24,'kcal/mol'),
        S298 = (70.92,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 438,
    label = "NH2OONH2",
    molecule = """
1 N 0 1 {3,S} {5,S} {6,S}
2 N 0 1 {4,S} {7,S} {8,S}
3 O 0 2 {1,S} {4,S}
4 O 0 2 {2,S} {3,S}
5 H 0 0 {1,S}
6 H 0 0 {1,S}
7 H 0 0 {2,S}
8 H 0 0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.82,25.88,27.94,29.70,32.52,34.58,37.65],'cal/(mol*K)'),
        H298 = (34.83,'kcal/mol'),
        S298 = (73.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 439,
    label = "NH2NHNHNH2",
    molecule = """
1 N 0 1 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 N 0 1 {1,S} {5,S} {6,S}
5 H 0 0 {4,S}
6 N 0 1 {4,S} {7,S} {8,S}
7 H 0 0 {6,S}
8 N 0 1 {6,S} {9,S} {10,S}
9 H 0 0 {8,S}
10 H 0 0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.46,26.65,30.82,34.00,38.75,41.98,46.14],'cal/(mol*K)'),
        H298 = (70.00,'kcal/mol'),
        S298 = (71.55,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 440,
    label = "NH2NHOH",
    molecule = """
1 N 0 1 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 N 0 1 {1,S} {5,S} {6,S}
5 H 0 0 {4,S}
6 O 0 2 {4,S} {7,S}
7 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.82,18.27,21.35,23.86,27.43,29.80,32.56],'cal/(mol*K)'),
        H298 = (9.84,'kcal/mol'),
        S298 = (63.03,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 441,
    label = "N_NH2_3",
    molecule = """
1 N 0 1 {2,S} {5,S} {8,S}
2 N 0 1 {1,S} {3,S} {4,S}
3 H 0 0 {2,S}
4 H 0 0 {2,S}
5 N 0 1 {1,S} {6,S} {7,S}
6 H 0 0 {5,S}
7 H 0 0 {5,S}
8 N 0 1 {1,S} {9,S} {10,S}
9 H 0 0 {8,S}
10 H 0 0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.56,25.03,28.72,31.87,36.84,40.39,45.35],'cal/(mol*K)'),
        H298 = (66.12,'kcal/mol'),
        S298 = (73.40,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 442,
    label = "NH2ON_H_O_OH",
    molecule = """
1 N 0 1 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 O 0 2 {1,S} {5,S}
5 N 0 0 {4,S} {6,S} {7,S} {8,S}
6 H 0 0 {5,S}
7 O 0 3 {5,S}
8 O 0 2 {5,S} {9,S}
9 H 0 0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([23.49,26.59,29.54,32.12,36.24,39.25,43.55],'cal/(mol*K)'),
        H298 = (8.18,'kcal/mol'),
        S298 = (111.00,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC; scans 2, 3 rigid
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 443,
    label = "NH2NH_O_OH",
    molecule = """
1 N 0 1 {2,S} {3,S} {4,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 N 0 0 {1,S} {5,S} {6,S} {7,S}
5 H 0 0 {4,S}
6 O 0 3 {4,S}
7 O 0 2 {4,S} {8,S}
8 H 0 0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.68,22.81,25.48,27.77,31.36,33.90,37.40],'cal/(mol*K)'),
        H298 = (7.23,'kcal/mol'),
        S298 = (71.23,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC; scan 2 rigid
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 444,
    label = "HNN_O_OH_r1",
    molecule = """
1 H 0 0 {2,S}
2 O 0 2 {1,S} {3,S}
3 N 0 0 {2,S} {4,S} {5,D}
4 O 0 3 {3,S}
5 N 0 1 {3,D} {6,S}
6 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.32,18.25,20.64,22.46,25.10,26.78,28.63],'cal/(mol*K)'),
        H298 = (11.55,'kcal/mol'),
        S298 = (66.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 445,
    label = "HNN_O_OH_r2",
    molecule = """
1 H 0 0 {2,S}
2 O 0 2 {1,S} {3,S}
3 N 0 0 {2,S} {4,D} {5,S}
4 O 0 2 {3,D}
5 N 0 2 {3,S} {6,S}
6 H 0 0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.32,18.25,20.64,22.46,25.10,26.78,28.63],'cal/(mol*K)'),
        H298 = (11.55,'kcal/mol'),
        S298 = (66.54,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 446,
    label = "N_OH_3",
    molecule = """
1 N 0 1 {2,S} {4,S} {6,S}
2 O 0 2 {1,S} {3,S}
3 H 0 0 {2,S}
4 O 0 2 {1,S} {5,S}
5 H 0 0 {4,S}
6 O 0 2 {1,S} {7,S}
7 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([20.43,23.87,25.91,27.07,28.69,29.74,31.17],'cal/(mol*K)'),
        H298 = (-39.54,'kcal/mol'),
        S298 = (70.40,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC; rigid scan 2
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 447,
    label = "N_NH2_OH_2",
    molecule = """
1 N 0 1 {2,S} {4,S} {6,S}
2 O 0 2 {1,S} {3,S}
3 H 0 0 {2,S}
4 O 0 2 {1,S} {5,S}
5 H 0 0 {4,S}
6 N 0 1 {1,S} {7,S} {8,S}
7 H 0 0 {6,S}
8 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([24.04,26.63,28.79,30.59,33.35,35.20,37.49],'cal/(mol*K)'),
        H298 = (-3.46,'kcal/mol'),
        S298 = (139.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 448,
    label = "N_NH2_2_OH",
    molecule = """
1 N 0 1 {2,S} {4,S} {7,S}
2 O 0 2 {1,S} {3,S}
3 H 0 0 {2,S}
4 N 0 1 {1,S} {5,S} {6,S}
5 H 0 0 {4,S}
6 H 0 0 {4,S}
7 N 0 1 {1,S} {8,S} {9,S}
8 H 0 0 {7,S}
9 H 0 0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.30,25.63,28.23,30.46,33.99,36.52,40.20],'cal/(mol*K)'),
        H298 = (30.33,'kcal/mol'),
        S298 = (73.56,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 449,
    label = "NH3NOH",
    molecule = """
1 N 0 0 {2,S} {3,S} {4,S} {5,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 H 0 0 {1,S}
5 N 0 2 {1,S} {6,S}
6 O 0 2 {5,S} {7,S}
7 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.64,18.66,20.39,21.93,24.61,26.78,30.33],'cal/(mol*K)'),
        H298 = (52.59,'kcal/mol'),
        S298 = (99.83,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 450,
    label = "N_H_NH_NH2_2",
    molecule = """
1 N 0 0 {2,S} {4,S} {7,S} {10,S}
2 N 0 2 {1,S} {3,S}
3 H 0 0 {2,S}
4 N 0 1 {1,S} {5,S} {6,S}
5 H 0 0 {4,S}
6 H 0 0 {4,S}
7 N 0 1 {1,S} {8,S} {9,S}
8 H 0 0 {7,S}
9 H 0 0 {7,S}
10 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([21.54,25.32,28.62,31.49,36.13,39.57,44.75],'cal/(mol*K)'),
        H298 = (100.87,'kcal/mol'),
        S298 = (74.64,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 451,
    label = "HOOOH",
    molecule = """
1 H 0 0 {2,S}
2 O 0 2 {1,S} {3,S}
3 O 0 2 {2,S} {4,S}
4 O 0 2 {3,S} {5,S}
5 H 0 0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.12,19.08,20.64,21.84,23.40,24.12,24.11],'cal/(mol*K)'),
        H298 = (-20.98,'kcal/mol'),
        S298 = (129.98,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 452,
    label = "N_O_OH_3",
    molecule = """
1 N 0 0 {2,S} {4,S} {6,S} {8,S}
2 O 0 2 {1,S} {3,S}
3 H 0 0 {2,S}
4 O 0 2 {1,S} {5,S}
5 H 0 0 {4,S}
6 O 0 2 {1,S} {7,S}
7 H 0 0 {6,S}
8 O 0 3 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.98,26.67,29.04,30.93,33.77,35.67,37.99],'cal/(mol*K)'),
        H298 = (-44.36,'kcal/mol'),
        S298 = (74.99,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC; rigid scan 1, 2, 3; scan 3 finds slightly lower but unstable minimum
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 453,
    label = "N_NH_OH_3",
    molecule = """
1 N 0 0 {2,S} {4,S} {6,S} {8,S}
2 O 0 2 {1,S} {3,S}
3 H 0 0 {2,S}
4 O 0 2 {1,S} {5,S}
5 H 0 0 {4,S}
6 O 0 2 {1,S} {7,S}
7 H 0 0 {6,S}
8 N 0 2 {1,S} {9,S}
9 H 0 0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([25.48,30.01,33.29,36.03,40.20,43.01,46.36],'cal/(mol*K)'),
        H298 = (10.69,'kcal/mol'),
        S298 = (107.11,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC;rigid scan 1, 2, 3, 4
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 454,
    label = "N_NH2_2_O_OH",
    molecule = """
1 N 0 0 {2,S} {4,S} {7,S} {10,S}
2 O 0 2 {1,S} {3,S}
3 H 0 0 {2,S}
4 N 0 1 {1,S} {5,S} {6,S}
5 H 0 0 {4,S}
6 H 0 0 {4,S}
7 N 0 1 {1,S} {8,S} {9,S}
8 H 0 0 {7,S}
9 H 0 0 {7,S}
10 O 0 3 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([22.14,27.45,31.59,34.66,39.12,42.07,45.69],'cal/(mol*K)'),
        H298 = (22.41,'kcal/mol'),
        S298 = (72.28,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC; rigid scan 2, scan 3 cosine fit
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 455,
    label = "N_H_NH_NH2_OH",
    molecule = """
1 N 0 0 {2,S} {4,S} {7,S} {9,S}
2 N 0 2 {1,S} {3,S}
3 H 0 0 {2,S}
4 N 0 1 {1,S} {5,S} {6,S}
5 H 0 0 {4,S}
6 H 0 0 {4,S}
7 O 0 2 {1,S} {8,S}
8 H 0 0 {7,S}
9 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.78,24.22,27.78,30.62,35.08,38.24,42.66],'cal/(mol*K)'),
        H298 = (55.93,'kcal/mol'),
        S298 = (102.03,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC; rigid scan 1, 2, 3; scan 3 finds slightly lower but unstable minimum
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 456,
    label = "N_H_2_NH_NH2",
    molecule = """
1 N 0 0 {2,S} {4,S} {7,S} {8,S}
2 N 0 2 {1,S} {3,S}
3 H 0 0 {2,S}
4 N 0 1 {1,S} {5,S} {6,S}
5 H 0 0 {4,S}
6 H 0 0 {4,S}
7 H 0 0 {1,S}
8 H 0 0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([19.26,22.50,25.31,27.70,31.40,33.96,37.29],'cal/(mol*K)'),
        H298 = (84.20,'kcal/mol'),
        S298 = (129.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 457,
    label = "N_H_2_O_OH",
    molecule = """
1 N 0 0 {2,S} {3,S} {4,S} {6,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 O 0 2 {1,S} {5,S}
5 H 0 0 {4,S}
6 O 0 3 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([12.90,15.22,17.31,19.12,22.00,24.08,27.01],'cal/(mol*K)'),
        H298 = (-6.78,'kcal/mol'),
        S298 = (62.29,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 458,
    label = "HONNN",
    molecule = """
1 H 0 0 {2,S}
2 O 0 2 {1,S} {3,S}
3 N 0 1 {2,S} {4,D}
4 N 0 0 {3,D} {5,D}
5 N 0 2 {4,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([14.41,16.40,17.99,19.17,20.85,21.99,23.39],'cal/(mol*K)'),
        H298 = (72.13,'kcal/mol'),
        S298 = (65.43,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 459,
    label = "N_H_2_NH2_O",
    molecule = """
1 N 0 0 {2,S} {3,S} {4,S} {7,S}
2 H 0 0 {1,S}
3 H 0 0 {1,S}
4 N 0 1 {1,S} {5,S} {6,S}
5 H 0 0 {4,S}
6 H 0 0 {4,S}
7 O 0 3 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([15.96,18.60,21.06,23.30,26.92,29.38,32.57],'cal/(mol*K)'),
        H298 = (30.76,'kcal/mol'),
        S298 = (94.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 460,
    label = "N_H_NH_O_r1",
    molecule = """
1 N 0 0 {2,S} {3,D} {5,S}
2 H 0 0 {1,S}
3 N 0 1 {1,D} {4,S}
4 H 0 0 {3,S}
5 O 0 3 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.06,13.22,15.18,16.79,19.12,20.77,23.05],'cal/(mol*K)'),
        H298 = (28.59,'kcal/mol'),
        S298 = (59.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 461,
    label = "N_H_NH_O_r2",
    molecule = """
1 N 0 0 {2,S} {3,S} {5,D}
2 H 0 0 {1,S}
3 N 0 2 {1,S} {4,S}
4 H 0 0 {3,S}
5 O 0 2 {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([11.06,13.22,15.18,16.79,19.12,20.77,23.05],'cal/(mol*K)'),
        H298 = (28.59,'kcal/mol'),
        S298 = (59.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 462,
    label = "HNNHNOH_r1",
    molecule = """
1 H 0 0 {2,S}
2 N 0 1 {1,S} {3,D}
3 N 0 0 {2,D} {4,S} {5,S}
4 H 0 0 {3,S}
5 N 0 2 {3,S} {6,S}
6 O 0 2 {5,S} {7,S}
7 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.19,19.52,22.38,24.79,28.48,30.98,33.95],'cal/(mol*K)'),
        H298 = (55.87,'kcal/mol'),
        S298 = (66.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 463,
    label = "HNNHNOH_r2",
    molecule = """
1 H 0 0 {2,S}
2 N 0 2 {1,S} {3,S}
3 N 0 0 {2,S} {4,S} {5,D}
4 H 0 0 {3,S}
5 N 0 1 {3,D} {6,S}
6 O 0 2 {5,S} {7,S}
7 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([16.19,19.52,22.38,24.79,28.48,30.98,33.95],'cal/(mol*K)'),
        H298 = (55.87,'kcal/mol'),
        S298 = (66.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 464,
    label = "HNN_O_NO_r1",
    molecule = """
1 H 0 0 {2,S}
2 N 0 1 {1,S} {3,D}
3 N 0 0 {2,D} {4,S} {5,S}
4 O 0 3 {3,S}
5 N 0 1 {3,S} {6,D}
6 O 0 2 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.91,21.12,22.89,24.37,26.59,28.04,29.72],'cal/(mol*K)'),
        H298 = (61.59,'kcal/mol'),
        S298 = (105.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 465,
    label = "HNN_O_NO_r2",
    molecule = """
1 H 0 0 {2,S}
2 N 0 2 {1,S} {3,S}
3 N 0 0 {2,S} {4,D} {5,S}
4 O 0 2 {3,D}
5 N 0 1 {3,S} {6,D}
6 O 0 2 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([18.91,21.12,22.89,24.37,26.59,28.04,29.72],'cal/(mol*K)'),
        H298 = (61.59,'kcal/mol'),
        S298 = (105.94,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 466,
    label = "N_NO2_cNHO_O",
    molecule =         """
1 N 0 0 {2,S} {3,S} {4,S} {5,S}
2 N 0 1 {1,S} {4,S} {6,S}
3 N 0 0 {1,S} {7,D} {8,S}
4 O 0 2 {1,S} {2,S}
5 O 0 3 {1,S}
6 H 0 0 {2,S}
7 O 0 2 {3,D}
8 O 0 3 {3,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([29.10,31.77,33.99,35.78,38.29,39.72,40.74],'cal/(mol*K)'),
        H298 = (87.38,'kcal/mol'),
        S298 = (227.12,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC; restrained distances between atoms 1, 3, 5 for optimization
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 468,
    label = "N_cNHO_O_ONO2",
    molecule =         """
        1 N 0 1 {2,S} {4,S} {5,S}
        2 N 0 1 {1,S} {4,S} {6,S}
        3 N 0 0 {5,S} {7,D} {8,S}
        4 O 0 2 {1,S} {2,S}
        5 O 0 2 {1,S} {3,S}
        6 H 0 0 {2,S}
        7 O 0 2 {3,D}
        8 O 0 3 {3,S}
        """,
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([31.43,35.17,38.24,40.73,44.24,46.28,47.84],'cal/(mol*K)'),
        H298 = (106.33,'kcal/mol'),
        S298 = (255.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC; restrained distances between atoms 1, 3, 4 for optimization, only used rotor 2, rotor 1 leads to error in CanTherm
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)

entry(
    index = 469,
    label = "N_NH_2_NH2",
    molecule = """
1 N 0 0 {2,S} {4,D} {6,S}
2 N 0 2 {1,S} {3,S}
3 H 0 0 {2,S}
4 N 0 1 {1,D} {5,S}
5 H 0 0 {4,S}
6 N 0 1 {1,S} {7,S} {8,S}
7 H 0 0 {6,S}
8 H 0 0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([17.80,21.25,24.01,26.35,30.10,32.84,36.88],'cal/(mol*K)'),
        H298 = (90.46,'kcal/mol'),
        S298 = (69.47,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
 level of theory: CCSD(T)F12A/cc-pVTZ-F12//B3LYP/6-311++g(d,p) + BAC
""",
    history = [
        ("Mon Nov 18 10:25:25 2012","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this value."""),
    ],
)
