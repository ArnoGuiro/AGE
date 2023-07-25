# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 12:18:46 2022

@author: Arnaud
"""
import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud as wc

#https://www.python-graph-gallery.com/wordcloud/

text_cloud = ('authenticité travail ambition rigueur pragmatisme bienveillance serieux courage détermination formation fierté apprentissage amélioration_continue professionalisme leadership initiative accomplissement respect ponctualité discipline cohérence créativité service')

wordcloud = wc(width = 7000, height = 1500, margin=0, random_state=1, background_color='white', 
               colormap='Set2', collocations=False).generate(text_cloud)


plt.figure(figsize=(30,7))
plt.imshow(wordcloud)
plt.axis('off')

plt.savefig('p_image_cloud.jpg')





