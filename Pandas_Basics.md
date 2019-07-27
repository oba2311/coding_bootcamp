# Pandas Basics:

Pandas is one of Python immensely useful tools. Usually this library is imported in the following way:
```
import pandas as pd
```

### Types and numpy:
In order to extract values from panda's dataframe (I'll be using df to call dataframe):
```
np_vals = df.values #yields numpy ndarray values.
```

Notice that the two libraries work together like magic:
```
result = np.method(pandas_df) #yields a new df after executing the numpy method on the panda's df.
```

### Python dicts and insertion:
We can push python's dicts onto a pd df:

```
python_data_dict = {
      musks_comp:['Tesla',
                  'SpaceX',
                  'Neuralink']  ,
      why_be_worried:['smoking weed live',
                      'too much to manage',
                      'etc']
                    }
```

This can be pushed onto a pd df like so:
```
df = pd.DataFrame(python_data_dict)
```

### Subset rows / cols & Checking heads and tails:
They way we can present specific rows and columns is the following:

```
df.head() #will spit out the first few rows of the df.
df.tail() #will spit out the last few rows of the df.
```

To get only specific columns:
```
df[['col_1', 'col_2']] #gets us the desired columns with all respective rows.`
```

To get only specific rows:
```
df[from_this_row_#:to_this_row_#]
```

Extract results based on conditions(filtering):
```
df[df['some_col'] > some_condition]
```


### Tweaking index and col names:
```
df.index = ['list','of','indices names'] # or df.set_index('col_name', inplace=True)
```
and
```
df.columns = ['list','of','col names']
```

### Sneak peek to the data:
A very useful way to get an overview of the df:

```
df.describe() #will present descriptive stats for the df
```

### Handling missing values:
```
# would fill in with the desired value instead of NaN (Not a Numder)
df.fillna(desired_value)
```
This idea can be further developed to fill in each column's NaNs differencetly:
```
df.fillna({
  'col_1_name': value,
  'col_2_name': other_value,
  'etc_3' : yet_another_value
  })
```

(More advanced methods to fill in data gaps coming in another post. such as
  ```
  df.ffil(),
  df.bfil()
  df.interpolate()
  df.dropna()

  ```
  )
