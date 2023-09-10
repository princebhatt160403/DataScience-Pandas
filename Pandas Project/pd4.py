import pandas as pd
import numpy as np
exam_data = {
    'name': ['Vanshika', 'Prince', 'Rishi', 'Anshita', 'Honey', 'Yash', 'Boi', 'Laura', 'Virat', 'Rahul'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
}
df = pd.DataFrame(exam_data)
selected_columns = df[['name', 'score']]
print(selected_columns)
