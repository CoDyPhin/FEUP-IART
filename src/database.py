from board import *
easy_db = ( #*Few milisseconds
    Board([
        [['o','gP'],        ['o','-'],     ['gC','-'],     ['o','gP']],
        [['o','-'],        ['o','-'],      ['gC','-'],    ['o','-']],
        [['o','-'],         ['o','-'],      ['o','-'],     ['x','x']],
        [['x', 'x'],        ['x', 'x'],     ['o','-'],     ['x','x']]
    ]),

    Board([
        [['o','-'],        ['o','bP'],     ['x', 'x'],     ['x', 'x']],
        [['o','bP'],        ['o','-'],      ['o','-'],    ['o','-']],
        [['bC','-'],         ['x', 'x'],      ['bC','-'],     ['o','-']],
        [['x', 'x'],        ['o','-'],     ['x', 'x'],     ['o','-']]
    ]),

    Board([
        [['o','-'],        ['o','bP'],      ['o','-'],     ['o','-']],
        [['o','-'],        ['o','bP'],      ['o','-'],     ['bC','-']],
        [['o','-'],        ['x','x'],       ['x','x'],     ['o','-']],
        [['o','-'],        ['o','-'],       ['o','-'],     ['bC','-']]
    ]),

    Board([
        [['o','-'],        ['o','-'],     ['o','-'],     ['gC','-']],
        [['o','-'],        ['x','x'],      ['x','x'],    ['o','-']],
        [['o','-'],         ['o','-'],      ['o','gP'],     ['o','-']],
        [['o','gP'],        ['o','-'],     ['o','-'],     ['gC','-']]

    ]),
    Board([
        [['pC','-'],        ['pC','-'],     ['x','x'],     ['o','-'],   ['x','x']],
        [['o','-'],        ['x','x'],      ['x','x'],    ['o','-'],     ['o','-']],
        [['o','pP'],         ['o','-'],      ['o','-'],     ['o','-'],   ['x','x']],
        [['x', 'x'],        ['o', '-'],     ['o','-'],     ['o','-'],   ['o','-']],
        [['o','pP'],         ['o','-'],      ['o','-'],     ['o','-'],   ['o','-']]

    ]),
    
    Board([
        [['x','x'],        ['o','yP'],     ['x','x'],     ['rC','-']],
        [['x','x'],        ['o','rP'],      ['yC','-'],    ['o','-']],
        [['x','x'],         ['o','-'],      ['o','-'],     ['x','x']],
        [['o','-'],        ['x','x'],     ['x','x'],     ['o','-']]
    ]),
    
    Board([
        [['x','x'],        ['o','-'],     ['o','-'],     ['bC','-']],
        [['x','x'],        ['o','-'],      ['x','x'],    ['x','x']],
        [['o','-'],         ['o','rP'],      ['o','-'],     ['rC','-']],
        [['o','-'],        ['o','-'],     ['x','x'],     ['o','bP']]
    ]),
    
    Board([
        [['rC','-'],        ['o','-'],     ['x','x'],     ['x','x']],
        [['yC','-'],        ['o','-'],      ['o','rP'],    ['o','yP']],
        [['o','-'],         ['x','x'],      ['x','x'],     ['x','x']],
        [['o','-'],        ['x','x'],     ['o','-'],     ['x','x']]
    ]),

    Board([
        [['o','-'],        ['o','yP'],     ['o','-'],     ['o','-'],   ['rC','-'],   ['x','x']],
        [['o','-'],        ['o','-'],      ['o','-'],    ['o','-'],     ['o','-'],   ['gC','-']],
        [['o','-'],         ['x','x'],      ['o','-'],     ['x','x'],   ['o','-'],   ['o','gP']],
        [['o', '-'],        ['o', '-'],     ['o','rP'],     ['o','-'],   ['x','x'],   ['x','x']],
        [['x','x'],         ['o','-'],      ['o','-'],     ['o','-'],   ['o','-'],   ['x','x']],
        [['yC','-'],        ['o','-'],      ['o','-'],    ['o','-'],     ['x','x'],   ['o','-']]
    ])
    
)

medium_db = (       #* 5 - 40 secs
    Board([
        [['o','-'],        ['x','x'],     ['o','-'],     ['yC','-']],
        [['o','-'],        ['x','x'],      ['o','-'],    ['x','x']],
        [['o','yP'],         ['o','-'],      ['o','-'],     ['o','-']],
        [['yC','-'],        ['o','yP'],     ['o','-'],     ['o','-']]

    ]),

    Board([
        [['x','x'],        ['o','-'],     ['x','x'],     ['o','-'],   ['o','-'],   ['o','bP']],
        [['x','x'],        ['x','x'],      ['o','-'],    ['x','x'],     ['o','-'],   ['o','-']],
        [['bC','-'],         ['o','yP'],      ['o','-'],     ['o','-'],   ['o','-'],   ['o','-']],
        [['o', 'rP'],        ['o', '-'],     ['o','-'],     ['o','-'],   ['x','x'],   ['o','-']],
        [['x','x'],         ['x','x'],      ['o','-'],     ['o','-'],   ['o','-'],   ['o','-']],
        [['rC','-'],        ['yC','-'],      ['o','-'],    ['x','x'],     ['o','-'],   ['x','x']]
    ]),

    Board([
        [['x','x'],        ['o','-'],     ['o','-'],     ['o','-'],   ['o','-'],   ['gC','-']],
        [['o','pP'],        ['o','-'],      ['o','-'],    ['rC','-'],     ['x','x'],   ['x','x']],
        [['o','gP'],         ['o','-'],      ['o','-'],     ['o','-'],   ['o','-'],   ['pC','-']],
        [['o', '-'],        ['x', 'x'],     ['o','-'],     ['o','-'],   ['o','-'],   ['x','x']],
        [['o','-'],         ['o','-'],      ['o','-'],     ['x','x'],   ['o','-'],   ['o','-']],
        [['o','-'],        ['o','rP'],      ['o','-'],    ['o','-'],     ['o','-'],   ['o','-']]
    ]),


    Board([
        [['o','-'],        ['x','x'],     ['pC','-'],     ['o','-']],
        [['o','-'],        ['o','pP'],      ['x','x'],    ['o','-']],
        [['o','-'],         ['x','x'],      ['o','-'],     ['o','-']],
        [['o', '-'],        ['o', 'pP'],     ['pC','-'],     ['o','-']]

    ]),
    
    Board([
        [['o','-'],        ['o','-'],     ['o','rP'],     ['x','x'],   ['o','-'],   ['x','x']],
        [['o','pP'],        ['o','-'],      ['o','-'],    ['o','-'],     ['o','-'],   ['o','-']],
        [['o','-'],         ['x','x'],      ['o','-'],     ['x','x'],   ['o','-'],   ['o','-']],
        [['o', '-'],        ['rC', '-'],     ['x','x'],     ['o','-'],   ['x','x'],   ['o','-']],
        [['bC','-'],         ['x','x'],      ['o','-'],     ['o','-'],   ['x','x'],   ['o','-']],
        [['o','bP'],        ['o','-'],      ['o','-'],    ['pC','-'],     ['x','x'],   ['o','-']]
    ]),
    
    Board([
        [['x','x'],        ['x','x'],     ['o','-'],     ['x','x'],   ['o','-']],
        [['o','-'],        ['o','-'],      ['x','x'],    ['x','x'],     ['o','-']],
        [['o','-'],         ['o','-'],      ['o','-'],     ['o','-'],   ['bC','-']],
        [['o', '-'],        ['x', 'x'],     ['x','x'],     ['o','-'],   ['o','bP']],
        [['o','bP'],         ['bC','-'],      ['x','x'],     ['x','x'],   ['x','x']]


    ]),
    Board([
        [['o','-'],        ['x','x'],     ['x','x'],     ['x','x'],   ['o','-']],
        [['o','-'],        ['x','x'],      ['x','x'],    ['o','-'],     ['x','x']],
        [['o','rP'],         ['o','-'],      ['x','x'],     ['rC','-'],   ['o','rP']],
        [['x', 'x'],        ['o', '-'],     ['o','-'],     ['rC','-'],   ['o','-']],
        [['o','-'],         ['x','x'],      ['o','-'],     ['x','x'],   ['o','-']]

    ]),
    Board([
        [['o','-'],        ['o','-'],     ['o','-'],     ['o','-'],   ['o','-']],
        [['o','-'],        ['o','pP'],      ['x','x'],    ['o','-'],     ['o','-']],
        [['o','-'],         ['x','x'],      ['o','-'],     ['o','-'],   ['o','-']],
        [['o', '-'],        ['o', '-'],     ['o','-'],     ['o','-'],   ['x','x']],
        [['x','x'],         ['o','pP'],      ['pC','-'],     ['pC','-'],   ['o','-']]

    ]),
    Board([
        [['o','-'],        ['o','-'],     ['o','-'],     ['o','-'],   ['o','-']],
        [['x','x'],        ['o','-'],      ['o','-'],    ['x','x'],     ['o','gP']],
        [['x','x'],         ['o','-'],      ['o','-'],     ['o','-'],   ['o','gP']],
        [['x', 'x'],        ['o', '-'],     ['x','x'],     ['o','-'],   ['x','x']],
        [['x','x'],         ['gC','-'],      ['x','x'],     ['o','-'],   ['gC','-']]
    ]),
    Board([
        [['o','-'],        ['o','-'],     ['yC','rP'],     ['x','x']],
        [['x','x'],        ['o','-'],      ['o','-'],    ['o','yP']],
        [['o','-'],         ['o','-'],      ['o','-'],     ['rC','-']],
        [['x','x'],        ['x','x'],     ['x','x'],     ['x','x']]
    ]),
    Board([
        [['o','-'],        ['o','gP'],     ['o','rP'],     ['o','-']],
        [['o','-'],        ['o','-'],      ['x','x'],    ['x','x']],
        [['o','-'],         ['o','-'],      ['o','-'],     ['o','-']],
        [['rC','-'],        ['gC','-'],     ['o','-'],     ['x','x']]
    ]),
    Board([
        [['o','-'],        ['o','-'],     ['x','x'],     ['x','x'],   ['o','-']],
        [['o','-'],        ['o','-'],      ['o','pP'],    ['x','x'],     ['o','-']],
        [['x','x'],         ['x','x'],      ['o','-'],     ['bC','-'],   ['o','-']],
        [['x', 'x'],        ['o', 'bP'],     ['o','-'],     ['o','-'],   ['o','-']],
        [['pC','-'],         ['o','-'],      ['x','x'],     ['o','-'],   ['x','x']]

    ]),
    
    Board([
        [['o','-'],        ['x','x'],     ['o','-'],     ['x','x'],   ['o','-']],
        [['x','x'],        ['o','rP'],      ['x','x'],    ['o','-'],     ['o','-']],
        [['x','x'],         ['o','-'],      ['x','x'],     ['o','-'],   ['rC','-']],
        [['x', 'x'],        ['o', '-'],     ['o','-'],     ['pC','-'],   ['x','x']],
        [['o','-'],         ['x','x'],      ['x','x'],     ['o','-'],   ['o','pP']]

    ]),
    
    Board([
        [['x','x'],        ['x','x'],     ['o','-'],     ['o','-'],   ['o','-'],   ['o','bP']],
        [['o','-'],        ['x','x'],      ['o','-'],    ['o','-'],     ['o','-'],   ['o','-']],
        [['o','-'],         ['o','rP'],      ['o','-'],     ['o','-'],   ['x','x'],   ['o','-']],
        [['o', '-'],        ['o', '-'],     ['o','-'],     ['o','-'],   ['x','x'],   ['o','pP']],
        [['o','-'],         ['x','x'],      ['pC','-'],     ['x','x'],   ['o','-'],   ['o','-']],
        [['o','-'],        ['o','-'],      ['bC','-'],    ['o','-'],     ['rC','-'],   ['x','x']]
    ]),
    
    Board([
        [['o','bP'],        ['o','-'],     ['o','-'],     ['o','-'],   ['o','-'],   ['x','x']],
        [['o','-'],        ['o','-'],      ['o','-'],    ['o','-'],     ['o','-'],   ['o','rP']],
        [['x','x'],         ['x','x'],      ['o','-'],     ['o','-'],   ['o','-'],   ['x','x']],
        [['o', '-'],        ['bC', '-'],     ['rC','-'],     ['x','x'],   ['x','x'],   ['o','-']],
        [['o','-'],         ['pC','-'],      ['x','x'],     ['o','-'],   ['o','pP'],   ['x','x']],
        [['x','x'],        ['o','-'],      ['o','-'],    ['o','-'],     ['o','-'],   ['o','-']]
    ]), 
    
    Board([
        [['x','x'],        ['o','-'],     ['o','rP'],     ['o','-'],   ['o','-'],   ['x','x']],
        [['o','-'],        ['o','bP'],      ['o','-'],   ['o','-'],     ['o','-'],   ['bC','-']],
        [['o','gP'],         ['gC','-'],      ['x','x'],     ['o','-'],   ['o','-'],   ['o','-']],
        [['rC','-'],        ['x', 'x'],    ['o','-'],     ['o','-'],   ['o','-'],   ['x','x']],
        [['o','-'],         ['o','-'],      ['x','x'],     ['o','-'],   ['o','-'],   ['x','x']],
        [['o','-'],       ['o','-'],     ['x','x'],    ['x','x'],     ['o','-'],   ['x','x']]

    ])
)

hard_db = (     #* 30 - 200 secs 
    Board([
        [['o','-'],        ['o','-'],     ['x','x'],     ['o','-'],   ['x','x']],
        [['o','pP'],        ['o','-'],      ['o','-'],    ['o','pP'],     ['o','-']],
        [['o','-'],         ['x','x'],      ['o','-'],     ['x','x'],   ['o','-']],
        [['o', '-'],        ['pC', '-'],     ['x','x'],     ['o','-'],   ['pC','-']],
        [['o','-'],         ['x','x'],      ['x','x'],     ['o','-'],   ['x','x']]
    ]),
    
    Board([
        [['o','-'],        ['o','pP'],     ['o','-'],     ['o','pP'],   ['o','-']],
        [['x','x'],        ['o','-'],      ['x','x'],    ['o','-'],     ['o','-']],
        [['x','x'],         ['x','x'],      ['o','-'],     ['o','-'],   ['x','x']],
        [['o', '-'],        ['pC', '-'],     ['o','-'],     ['o','-'],   ['pC','-']],
        [['x','x'],         ['o','-'],      ['o','-'],     ['x','x'],   ['o','-']]
    ]),
    
    Board([
        [['x','x'],        ['x','x'],     ['o','-'],     ['o','-'],   ['o','-']],
        [['o','-'],        ['o','-'],      ['o','-'],    ['x','x'],     ['o','-']],
        [['rC','-'],         ['o','-'],      ['o','rP'],     ['o','-'],   ['o','-']],
        [['rC', '-'],        ['o', '-'],     ['o','-'],     ['x','x'],   ['x','x']],
        [['x','x'],         ['o','rP'],      ['o','-'],     ['o','-'],   ['o','-']]
    ]),

    Board([
        [['o','-'],        ['o','-'],     ['o','-'],     ['x','x'],   ['o','-']],
        [['o','-'],        ['o','-'],      ['x','x'],    ['o','-'],     ['x','x']],
        [['bC','-'],         ['o','-'],      ['o','bP'],     ['o','-'],   ['o','-']],
        [['x', 'x'],        ['o', '-'],     ['x','x'],     ['x','x'],   ['o','-']],
        [['o','-'],         ['bC','-'],      ['o','bP'],     ['o','-'],   ['o','-']]
    ]),
    
    Board([
        [['x','x'],        ['o','-'],     ['o','-'],     ['x','x'],   ['o','-']],
        [['o','-'],        ['x','x'],      ['o','-'],    ['rC','-'],     ['x','x']],
        [['o','-'],         ['o','rP'],      ['o','-'],     ['x','x'],   ['rC','-']],
        [['x', 'x'],        ['o', '-'],     ['o','-'],     ['o','-'],   ['o','rP']],
        [['o','-'],         ['x','x'],      ['x','x'],     ['x','x'],   ['o','-']]
    ]),
    
    Board([
        [['o','-'],        ['x','x'],     ['o','-'],     ['o','-'],   ['o','-']],
        [['x','x'],        ['o','-'],      ['o','-'],    ['bC','-'],     ['x','x']],
        [['bC','-'],         ['x','x'],      ['o','-'],     ['o','-'],   ['o','bP']],
        [['o', '-'],        ['o', '-'],     ['o','-'],     ['x','x'],   ['o','-']],
        [['x','x'],         ['o','bP'],      ['o','-'],     ['o','-'],   ['o','-']]
    ]),

    Board([
        [['pC','-'],        ['o','-'],     ['o','-'],     ['o','-']],
        [['gC','-'],        ['o','-'],      ['x','x'],    ['o','-']],
        [['o','-'],         ['o','-'],      ['x','x'],     ['x','x']],
        [['o','-'],        ['o','gP'],     ['o','-'],     ['o','pP']]
    ]),
    
    Board([
        [['o','-'],        ['gC','-'],     ['x','x'],     ['o','-'],   ['o','rP']],
        [['o','-'],        ['o','-'],      ['rC','-'],    ['o','-'],     ['o','-']],
        [['o','-'],         ['o','-'],      ['o','-'],     ['x','x'],   ['o','gP']],
        [['o', '-'],        ['x', 'x'],     ['o','-'],     ['o','-'],   ['x','x']],
        [['o','-'],         ['o','-'],      ['o','-'],     ['x','x'],   ['o','-']]
    ]),
    
    Board([
        [['x','x'],        ['o','-'],     ['o','-'],     ['o','-'],   ['o','-'],   ['o','-']],
        [['o','-'],        ['x','x'],      ['o','yP'],    ['o','-'],     ['x','x'],   ['o','-']],
        [['o','-'],         ['x','x'],      ['o','rP'],     ['o','-'],   ['o','-'],   ['yC','-']],
        [['o', '-'],        ['o', '-'],     ['o','-'],     ['o','-'],   ['o','-'],   ['x','x']],
        [['pC','-'],         ['x','x'],      ['o','-'],     ['x','x'],   ['x','x'],   ['o','-']],
        [['o','-'],        ['o','-'],      ['o','pP'],    ['o','-'],     ['o','-'],   ['rC','-']]
    ])

)

"""staticboard = Board([[['o', 'gP'], ['o', '-'], ['o', '-'], ['o', '-'], ['o', '-']], [['gC', '-'], ['x', 'x'], ['o', '-'], ['x', 'x'], ['o', '-']], [['x', 'x'], ['x', 'x'], ['o', '-'], ['o', '-'], ['o', '-']], [['o', '-'], ['o', '-'], ['o', '-'], ['x', 'x'], ['o', '-']], [['bC', '-'], ['o', '-'], ['o', '-'], ['o', 'bP'], ['x', 'x']]])

        staticboard2 = Board([  [['x','x'],         ['x','x'],      ['x','x'],     ['x','x'],      ['o','-'],      ['x','x']],
                                [['x', 'x'],        ['o','rP'],     ['o','-'],     ['o','-'],      ['bC','-'],     ['x','x']],
                                [['o','-'],         ['o','-'],      ['rC','-'],    ['o','-'],      ['x','x'],      ['x','x']],
                                [['x','x'],         ['o','-'],      ['x','x'],     ['x','x'],      ['o','-'],      ['x','x']],
                                [['x','x'],         ['o','-'],      ['o','-'],     ['o','bP'],     ['x','x'],      ['x','x']],
                                [['o','gP'],        ['gC','-'],     ['x','x'],     ['x','x'],      ['x','x'],      ['x','x']]])

        staticboard3 = Board([  [['x', 'x'],        ['o','rP'],     ['o','-'],     ['o','-']],
                                [['bC','-'],        ['o','-'],      ['rC','-'],    ['o','bP']],
                                [['x','x'],         ['o','-'],      ['x','x'],     ['x','x']],
                                [['o','gP'],        ['gC','-'],     ['x','x'],     ['x','x']]])

        staticboard4 = Board([   [['o', 'bP'],        ['x','x'],     ['bC','-'],     ['o','-'],      ['o','bP']],
                                [['bC','-'],        ['o','-'],      ['o','-'],      ['o','-'],      ['x','x']],
                                [['o','-'],         ['o','-'],     ['o','-'],     ['o','-'],      ['o','-']],
                                [['x','x'],         ['x','x'],      ['x','x'],     ['o','-'],     ['o','-']],
                                [['o','-'],        ['x','x'],     ['x','x'],     ['o','-'],      ['o','-']]])

        boardfodido = Board([   [['o', '-'],       ['o','pP'],      ['o', '-'],     ['o','-'],      ['o', '-']],
                                [['x','x'],        ['o','-'],       ['o','-'],      ['o','-'],      ['x','x']],
                                [['pC','-'],       ['x','x'],       ['o','-'],      ['o','-'],      ['pC','-']],
                                [['o', '-'],       ['o', '-'],      ['o', 'pP'],    ['o','-'],      ['o','-']],
                                [['o','-'],        ['o', '-'],      ['x','x'],      ['o','-'],      ['o','-']]])"""