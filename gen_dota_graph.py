"""
Authors: David Lanigan and Marco Ordonez

Description: This code uses Zen Network Library to make a DOTA 2 character network in a gml file format

"""

import zen
import numpy
import csv


"""____________________Prepare Data__________________________"""


heroes = csv.reader(open('hero_names2.csv'))

heroes = [row for row in heroes]

#load text file with Dota Player Data

#match = numpy.loadtxt('6.86A3.txt')
match = numpy.loadtxt('6.86B3.txt')


def CreateDotaGraph(HeroesList,GameMatrix):

    
    matchPlayed = GameMatrix[0:113,:]
    matchWon = GameMatrix[113:,:]

    
    #"""____________________Create Graph_________________________"""

    shapeHeros = numpy.shape(HeroesList)
   
    G = zen.Graph()

    #Graph with names only
    for i in range(1,shapeHeros[0]):
        G.add_node(HeroesList[i][2])
        
    print G.nodes()
    #"""______________________Add Edges__________________________"""


    for i in range(len(G.nodes())):
        for j in range(len(G.nodes())):
            if i != j:
                if matchWon[i][j] > 0 and matchPlayed[i][j] > 0 and G.has_edge_(i,j) == False:
                    G.add_edge_(i,j)
                    weight = 0.5 - round(float(matchWon[i][j])/float(matchPlayed[i][j]),3)
                    G.set_weight(G.node_object(i),G.node_object(j),weight)

    return G



G = CreateDotaGraph(heroes,match)

filename = 'dota_full_B3_hero.gml'

zen.io.gml.write(G,filename)

