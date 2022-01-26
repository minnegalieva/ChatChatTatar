from torch.utils.data import DataLoader
from datasets import load_dataset
import datasets
import pandas as pd
import numpy as np
import transformers

def get_DailyDialog():
    
    dialog_ind = 0
    def get_sent_ids(dialog):
        nonlocal dialog_ind
        num_sent = len(dialog)
        sent_ids = list(zip(dialog, np.full(num_sent,dialog_ind), np.arange(num_sent)))
        dialog_ind +=1
        return sent_ids
    
    dataset = load_dataset('daily_dialog',split='train')
    dataset = dataset.to_pandas()
    sent_id = dataset['dialog'].apply(lambda x: get_sent_ids(x))
    dataset = pd.DataFrame(pd.Series.sum(sent_id), columns=['utter', 'dialog_id', 'utter_in_dialog'])
    dataset['utter_hashed'] = dataset.utter.apply(hash)
    grouped = dataset.groupby('utter_hashed')
    dataset = grouped.agg({'utter':max, 'dialog_id':lambda x: x.tolist(), 'utter_in_dialog':lambda x: x.tolist()})
    dataset.reset_index(inplace=True)
    return dataset