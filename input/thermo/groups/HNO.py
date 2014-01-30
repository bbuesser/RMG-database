#!/usr/bin/env python
# encoding: utf-8

name = "HNO"
shortDesc = u""
longDesc = u"""

"""
recommended = False

entry(
    index = -1,
    label = "R",
    group = 
"""
1 * R 0
""",
    thermo = None,
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 1,
    label = "O(H)(N)",
    group = 
"""
1 * O 0 2 {2,S} {3,S}
2   H 0   {1,S}
3   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 2,
    label = "O(H)(O)",
    group = 
"""
1 * O 0 2 {2,S} {3,S}
2   H 0   {1,S}
3   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 3,
    label = "O(N)(N)",
    group = 
"""
1 * O 0 2 {2,S} {3,S}
2   N 0   {1,S}
3   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 4,
    label = "O(N)(O)",
    group = 
"""
1 * O 0 2 {2,S} {3,S}
2   N 0   {1,S}
3   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 5,
    label = "O(O)(O)",
    group = 
"""
1 * O 0 2 {2,S} {3,S}
2   O 0   {1,S}
3   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 6,
    label = "O(N)",
    group = 
"""
1 * O 0 3 {2,S}
2   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 7,
    label = "O(=N)",
    group = 
"""
1 * O 0 2 {2,D}
2   N 0   {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 8,
    label = "N(H)(H)(N)",
    group = 
"""
1 * N 0 1 {2,S} {3,S} {4,S}
2   H 0   {1,S}
3   H 0   {1,S}
4   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 9,
    label = "N(H)(H)(O)",
    group = 
"""
1 * N 0 1 {2,S} {3,S} {4,S}
2   H 0   {1,S}
3   H 0   {1,S}
4   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 10,
    label = "N(H)(N)(N)",
    group = 
"""
1 * N 0 1 {2,S} {3,S} {4,S}
2   H 0   {1,S}
3   N 0   {1,S}
4   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 11,
    label = "N(H)(N)(O)",
    group = 
"""
1 * N 0 1 {2,S} {3,S} {4,S}
2   H 0   {1,S}
3   N 0   {1,S}
4   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 12,
    label = "N(H)(O)(O)",
    group = 
"""
1 * N 0 1 {2,S} {3,S} {4,S}
2   H 0   {1,S}
3   O 0   {1,S}
4   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 13,
    label = "N(N)(N)(N)",
    group = 
"""
1 * N 0 1 {2,S} {3,S} {4,S}
2   N 0   {1,S}
3   N 0   {1,S}
4   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 14,
    label = "N(N)(N)(O)",
    group = 
"""
1 * N 0 1 {2,S} {3,S} {4,S}
2   N 0   {1,S}
3   N 0   {1,S}
4   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 15,
    label = "N(N)(O)(O)",
    group = 
"""
1 * N 0 1 {2,S} {3,S} {4,S}
2   N 0   {1,S}
3   O 0   {1,S}
4   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 16,
    label = "N(O)(O)(O)",
    group = 
"""
1 * N 0 1 {2,S} {3,S} {4,S}
2   O 0   {1,S}
3   O 0   {1,S}
4   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 17,
    label = "N(=N)(H)",
    group = 
"""
1 * N 0 1 {2,D} {3,S}
2   N 0   {1,D}
3   H 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 18,
    label = "N(=N)(N)",
    group = 
"""
1 * N 0 1 {2,D} {3,S}
2   N 0   {1,D}
3   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 19,
    label = "N(=N)(O)",
    group = 
"""
1 * N 0 1 {2,D} {3,S}
2   N 0   {1,D}
3   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 20,
    label = "N(=O)(N)",
    group = 
"""
1 * N 0 1 {2,D} {3,S}
2   O 0   {1,D}
3   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 21,
    label = "N(=O)(O)",
    group = 
"""
1 * N 0 1 {2,D} {3,S}
2   O 0   {1,D}
3   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 22,
    label = "N(N)(H)(H)(O)",
    group = 
"""
1 * N 0 0 {2,S} {3,S} {4,S} {5,S}
2   N 0   {1,S}
3   H 0   {1,S}
4   H 0   {1,S}
5   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 23,
    label = "N(=N)(H)(N)",
    group = 
"""
1 * N 0 0 {2,D} {3,S} {4,S}
2   N 0   {1,D}
3   H 0   {1,S}
4   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 24,
    label = "N(=N)(H)(O)",
    group = 
"""
1 * N 0 0 {2,D} {3,S} {4,S}
2   N 0   {1,D}
3   H 0   {1,S}
4   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 25,
    label = "N(=N)(N)(N)",
    group = 
"""
1 * N 0 0 {2,D} {3,S} {4,S}
2   N 0   {1,D}
3   N 0   {1,S}
4   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 26,
    label = "N(=N)(N)(O)",
    group = 
"""
1 * N 0 0 {2,D} {3,S} {4,S}
2   N 0   {1,D}
3   N 0   {1,S}
4   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)
                    
entry(
    index = 27,
    label = "N(=N)(O)(O)",
    group = 
"""
1 * N 0 0 {2,D} {3,S} {4,S}
2   N 0   {1,D}
3   O 0   {1,S}
4   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 28,
    label = "N(=O)(H)(N)",
    group = 
"""
1 * N 0 0 {2,D} {3,S} {4,S}
2   O 0   {1,D}
3   H 0   {1,S}
4   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 29,
    label = "N(=O)(N)(N)",
    group = 
"""
1 * N 0 0 {2,D} {3,S} {4,S}
2   O 0   {1,D}
3   N 0   {1,S}
4   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 30,
    label = "N(=O)(N)(O)",
    group = 
"""
1 * N 0 0 {2,D} {3,S} {4,S}
2   O 0   {1,D}
3   O 0   {1,S}
4   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 31,
    label = "N(=O)(O)(O)",
    group = 
"""
1 * N 0 0 {2,D} {3,S} {4,S}
2   O 0   {1,D}
3   O 0   {1,S}
4   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 32,
    label = "N(=N)(=N)",
    group = 
"""
1 * N 0 0 {2,D} {3,D}
2   N 0   {1,D}
3   N 0   {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 33,
    label = "N(N)(H)(H)(H)",
    group = 
"""
1 * N 0 0 {2,S} {3,S} {4,S} {5,S}
2   N 0   {1,S}
3   H 0   {1,S}
4   H 0   {1,S}
5   H 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 34,
    label = "N(O)(O)(H)(H)",
    group = 
"""
1 * N 0 0 {2,S} {3,S} {4,S} {5,S}
2   O 0   {1,S}
3   O 0   {1,S}
4   H 0   {1,S}
5   H 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 35,
    label = "N(N)(O)(O)(H)",
    group = 
"""
1 * N 0 0 {2,S} {3,S} {4,S} {5,S}
2   N 0   {1,S}
3   O 0   {1,S}
4   O 0   {1,S}
5   H 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 36,
    label = "N(N)(N)(H)(H)",
    group = 
"""
1 * N 0 0 {2,S} {3,S} {4,S} {5,S}
2   N 0   {1,S}
3   N 0   {1,S}
4   H 0   {1,S}
5   H 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 37,
    label = "N(O)(O)(O)(O)",
    group = 
"""
1 * N 0 0 {2,S} {3,S} {4,S} {5,S}
2   O 0   {1,S}
3   O 0   {1,S}
4   O 0   {1,S}
5   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 38,
    label = "N(O)(O)(O)(H)",
    group = 
"""
1 * N 0 0 {2,S} {3,S} {4,S} {5,S}
2   O 0   {1,S}
3   O 0   {1,S}
4   O 0   {1,S}
5   H 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 39,
    label = "N(N)(O)(O)(O)",
    group = 
"""
1 * N 0 0 {2,S} {3,S} {4,S} {5,S}
2   N 0   {1,S}
3   O 0   {1,S}
4   O 0   {1,S}
5   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 40,
    label = "N(N)(N)(O)(O)",
    group = 
"""
1 * N 0 0 {2,S} {3,S} {4,S} {5,S}
2   N 0   {1,S}
3   N 0   {1,S}
4   O 0   {1,S}
5   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 41,
    label = "N(N)(N)(N)(H)",
    group = 
"""
1 * N 0 0 {2,S} {3,S} {4,S} {5,S}
2   N 0   {1,S}
3   N 0   {1,S}
4   N 0   {1,S}
5   H 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 42,
    label = "N(N)(N)(O)(H)",
    group = 
"""
1 * N 0 0 {2,S} {3,S} {4,S} {5,S}
2   N 0   {1,S}
3   N 0   {1,S}
4   O 0   {1,S}
5   H 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 43,
    label = "N(N)(H)",
    group = 
"""
1 * N 0 2 {2,S} {3,S}
2   N 0   {1,S}
3   H 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 44,
    label = "N(N)(O)",
    group = 
"""
1 * N 0 2 {2,S} {3,S}
2   N 0   {1,S}
3   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 45,
    label = "N(=N)",
    group = 
"""
1 * N 0 2 {2,D}
2   N 0   {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 46,
    label = "N(N)(N)",
    group = 
"""
1 * N 0 2 {2,S} {3,S}
2   N 0   {1,S}
3   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 47,
    label = "N(=N)(H)(H)",
    group = 
"""
1 * N 0 0 {2,D} {3,S} {4,S}
2   N 0   {1,D}
3   H 0   {1,S}
4   H 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 48,
    label = "N(#N)(N)",
    group = 
"""
1 * N 0 0 {2,T} {3,S}
2   N 0   {1,T}
3   N 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 49,
    label = "N(#N)(O)",
    group = 
"""
1 * N 0 0 {2,T} {3,S}
2   N 0   {1,T}
3   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 50,
    label = "N(=N)(=O)",
    group = 
"""
1 * N 0 0 {2,D} {3,D}
2   N 0   {1,D}
3   O 0   {1,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 51,
    label = "N(#N)(H)",
    group = 
"""
1 * N 0 0 {2,T} {3,S}
2   N 0   {1,T}
3   H 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

entry(
    index = 52,
    label = "N(N)(N)(N)(O)",
    group = 
"""
1 * N 0 0 {2,S} {3,S} {4,S} {5,S}
2   N 0   {1,S}
3   N 0   {1,S}
4   N 0   {1,S}
5   O 0   {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.0,0.0,0.0,0.0,0.0,0.0,0.0],'cal/(mol*K)'),
        H298 = (0.0,'kcal/mol'),
        S298 = (0.0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
    history = [
        ("Mon Jan 13 12:27:50 2014","Beat Buesser <bbuesser@mit.edu>","action","""Beat Buesser <bbuesser@mit.edu> created this entry."""),
    ],
)

tree(
"""
L1: R
    L2: O(H)(N)
    L2: O(H)(O)
    L2: O(N)(N)
    L2: O(N)(O)
    L2: O(O)(O)
    L2: O(N)
    L2: O(=N)
    L2: N(H)(H)(N)
    L2: N(H)(H)(O)
    L2: N(H)(N)(N)
    L2: N(H)(N)(O)
    L2: N(H)(O)(O)
    L2: N(N)(N)(N)
    L2: N(N)(N)(O)
    L2: N(N)(O)(O)
    L2: N(O)(O)(O)         
    L2: N(=N)(H)
    L2: N(=N)(N)
    L2: N(=N)(O)
    L2: N(=O)(N)
    L2: N(=O)(O)
    L2: N(N)(H)(H)(O)
    L2: N(=N)(H)(H)
    L2: N(=N)(H)(N)
    L2: N(=N)(H)(O)
    L2: N(=N)(N)(N)
    L2: N(=N)(N)(O)
    L2: N(=N)(O)(O)
    L2: N(=O)(H)(N)
    L2: N(=O)(N)(N)
    L2: N(=O)(N)(O)
    L2: N(=O)(O)(O)   
    L2: N(=N)(=N)
    L2: N(=N)(=O)
    L2: N(N)(N)
    L2: N(N)(H)(H)(H)
    L2: N(O)(O)(H)(H)
    L2: N(N)(O)(O)(H)
    L2: N(N)(N)(H)(H)
    L2: N(O)(O)(O)(O)
    L2: N(O)(O)(O)(H)
    L2: N(N)(O)(O)(O)
    L2: N(N)(N)(O)(O)
    L2: N(N)(N)(N)(O)
    L2: N(N)(N)(N)(H)
    L2: N(N)(N)(O)(H)
    L2: N(N)(H)
    L2: N(N)(O)
    L2: N(=N)
    L2: N(#N)(H)
    L2: N(#N)(N)
    L2: N(#N)(O)
"""
)



#tree(
#"""
#L1: R
#    L2: O
#        L3: O(Rs)(Rs)    
#            L4: O(H)(Rs)
#                L5: O(H)(N)
#                L5: O(H)(O)
#            L4: O(N)(Rs)
#                L5: O(N)(N)
#                L5: O(N)(O)
#            L4: O(O)(Rs)
#                L5: O(O)(O)
#        L3: O(=Rd)
#            L4: O(=N)
#    L2: N
#        L3: N(Rs)(Rs)(Rs)
#                    L6: N(H)(H)(N)
#                    L6: N(H)(H)(O)
#                    L6: N(H)(N)(N)
#                    L6: N(H)(N)(O)
#                    L6: N(H)(O)(O)
#                    L6: N(N)(N)(N)
#                    L6: N(N)(N)(O)
#                    L6: N(N)(O)(O)
#                    L6: N(O)(O)(O)         
#        L3: N(=Rd)(Rs)
#            L4: N(=N)(Rs)
#                L5: N(=N)(H)
#                L5: N(=N)(N)
#                L5: N(=N)(O)
#            L4: N(=O)(Rs)
#                L5: N(=O)(N)
#                L5: N(=O)(O)
#        L3: N(=Rd)(Rs)(Rs)
#            L4: N(=N)(Rs)(Rs)
#                L5: N(=N)(H)(Rs)
#                    L6: N(=N)(H)(N)
#                    L6: N(=N)(H)(O)
#                    L6: N(=N)(N)(N)
#                    L6: N(=N)(N)(O)
#                    L6: N(=N)(O)(O)
#            L4: N(=O)(Rs)(Rs)
#                    L6: N(=O)(H)(N)
#                    L6: N(=O)(N)(N)
#                    L6: N(=O)(N)(O)
#                    L6: N(=O)(O)(O)   
#        L3: N(=Rd)(=Rd)
#            L4: N(=N)(=N)
#"""
#)

