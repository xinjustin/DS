# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 08:49:37 2018

@author: justinxin
"""

''' Spooky NLP '''
'''https://www.kaggle.com/arthurtok/spooky-nlp-and-topic-modelling-tutorial'''





'''wordcloud generation '''


clean_mask=np.array(Image.open("../input/imagesforkernal/safe-zone.png"))
clean_mask=clean_mask[:,:,1]
#wordcloud for clean comments
subset=train[train.clean==True]
text=subset.comment_text.values
wc= WordCloud(background_color="black",max_words=2000,mask=clean_mask,stopwords=stopword)
wc.generate(" ".join(text))
plt.figure(figsize=(20,10))
plt.axis("off")
plt.title("Words frequented in Clean Comments", fontsize=20)
plt.imshow(wc.recolor(colormap= 'viridis' , random_state=17), alpha=0.98)
plt.show()