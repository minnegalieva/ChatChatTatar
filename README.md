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
| My wallet and my cell phone . |
| I think that I would enjoy the position but there isn't a lot of creativity involved . |
| Usually we have a month off . |
| how old is he today ? |
|Good morning . Vane Theater , at your service . |
| Sure . This is the one I will not hesitate to recommend . Its color and style is so attractive and also the quality is really reliable . |
| Would you like to withdraw any money ? |
| I'm off today . |
| There must be about 50 computers in here . |
| Well , considering your qualifications , we believe you would be a suitable candidate . |
| Oh , I'm afraid it's too expensive . Can you show me something cheaper ? |
| I have to be there before 1700 . |
|I didn't see you at Mr . Johnson's class today . |
| I'm sure the security is very tight.Probably they will make us walk through metal detectors like at the airport . |
