import pandas as pd
import numpy as np
exam_data = {
    'name': ['Vanshika', 'Prince', 'Rishi', 'Anshita', 'Honey', 'Yash', 'Boi', 'Laura', 'Virat', 'Rahul'],
    'score': [16.5, 9,12.4 , np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
first_3_rows = df.head(3)
print(first_3_rows)
