# Pandas Basics:

Pandas is one of Python immensely useful tools. Usually this library is imported in the following way:
`import pandas as pd`

### Types and numpy:
In order to extract values from panda's dataframe (I'll be using df to call dataframe):
`np_vals = df.values` <-- yields numpy values.

* notice that the two libraries work together like magic: <br>
`result = np.method(pdDataFrame)` <-- yields a new df after executing the numpy method on the panda's df.

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
`df = pd.DataFrame(python_data_dict)`

### Subset rows / cols & Checking heads and tails:
They way we can present specific rows and columns is the following:
`df[['col_1', 'col_2']] #gets us the desired columns with all respective rows.`
`df[row_start:row_finish,col_start:col_finish]`

`df.head()` will spit out the first few rows of the df.
`df.tail()` will spit out the last few rows of the df.



### Tweaking index and col names:
`df.index = ['list','of','indices names']`
and
`df.columns = ['list','of','col names']`

### sneak peek to the data:
A very useful way to get an overview of the df:

`df.describe() #will present describtive stats for the df` 


### Resources used:

<sup>1</sup> https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c
