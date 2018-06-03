# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 23:04:45 2018

@author: justinxin
"""

'''Somer's D '''


from sklearn.metrics.ranking import roc_auc_score, roc_curve
def somers_d(y_true, y_score, average="macro",sample_weight=None):
    return 2*roc_auc_score(y_true,y_score,average,sample_weight)-1





''' plot ROC curve '''


fpr,tpr, td= roc_curve(y_test,rf_new.predict(x_test))


plt.figure()
lw = 2
plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve' )
plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic example')
plt.legend(loc="lower right")
plt.show()