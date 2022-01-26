# NN-for-dialog-annotation

# Week 1

TODO:
 - Create a dataframe of utterances from Daily Dialog
 - Vectorize data by TF-IDF
 - Cluster obtained vectors using kNN and K-means algorithms
 - Analize clusters
 
 Done:
 - Created Daily_Dialog_loader.py which creates a dataframe of utterances from Daily Dialog train dataset.
I removed most redundancy in utterances through hashing them.<br>
Dataframe columns:
    * utter_hashed - hash for an utterance
    * utter - individual utterance
    * dialog_id - list of diaolog ids in which this utterance exists
    * utter_in_dialog - list of utterance positions positions in the dialog from dialog_id column
- Normalized utterances for TF-IDF vectorization.<br>
Some utterances vanished, some reduced to one simbol, I removed them since later they clustered with any utterance. 
-  Reduced dimentionality of vectors to visualize the data <br>
PCA-plot, umap plot (3d plot can be found...)
- Clustered utterances <br>

|Example TF-IDF neighbours|
|---|
| Does it bother you when you have to chew a lot ? |
| No , don't bother . |
| No . don ’ t bother . |
| What is bothering you ? |
| Don't bother . |
| No , don ’ t bother . It ’ s all right as it is . |
| What are you going to do ? Call my boss and chew him out ? |
| There will be 4 of us . |
| Don ’ t bother . I will help myself . |
| I'm sorry . Has it been bothering you ? |
| I'm sorry to have bothered you . |
| She's always bothering me . What should I do ? |
| Thank you . But I don't think I'll bother . |
| No , don't bother . I think I'm OK . |
|What's bothering that guy ? |

This cluster as others for TF-IDF vectorization base mostly on a single word, in the above case to the "bother". Better to switch to context based vectorizations.

# Week 2
TODO:
- Perform BERT embedding
Done:
- Encoded data.
- *Insert pics of dimentionality reduced data.* It is hard to tell what is the reasonable amout of clusters we can set. 3D plot of PCA shows two big clusters, 
UMAP shows several big clusters.
-Clustered vectorized data using kNN algorithm 

|Example BERT neighbours|
|---|
| Does it bother you when you have to chew a lot ? |
| Does it bother you when you eat something really sweet ? |
| Do you have a lot on your mind when you try to go to sleep ? |
| what do you use to eat it ? |
| Don't you feel dull ? |
| What do you do to deal with the stress ? |
|What stresses you out the most ? |
| Is there some reason why you can ’ t get enough sleep ? |
| How do you protect yourself from chapped lips ? |
| What do you normally eat ? |
| What things make you excited ? |
| Is this the only kind you have ? |
| Is that how you feel on the bus ? |
| Don't you feel dizzy when you have to get up ? |
| How late do you try to go to sleep ? |
