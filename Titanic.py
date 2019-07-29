import pandas as pd
import seaborn as sb
tatanic = sb.load_dataset('titanic')
tatanic.to_csv('titanic_new.csv', index = False)

titanic_new = pd.read_csv('titanic_new.csv')

