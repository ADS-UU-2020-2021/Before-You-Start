# Before-You-Start

## Stuff you have to do:
- Follow the lectures on Monday and Tuesday  
- Exams on Thursday and Friday  
- Colloquiums on Fridays  
- Reread the slides from the lectures and learn them well  
- Lab exercises  
- Play around with SQL and Python on your own  
- read the book (IMO not necessary)  
- Enroll in elective courses!  


## Elective Courses
You need to enroll into elective courses, the window is already open.  
These are the courses to choose from: https://www.uu.nl/masters/en/applied-data-science/courses  
Pick whatevery you want, you have 4 courses and thus at least 2 domains  


## Info this week
You need to look up related info in the book yourself. He was going to look which chapters are related but he'll forget to do so if we don't remind him.  
Edit: he forgot.  
It is thought that one would find related info in chapter 3 to 8.  
The book is added to the repo.  
The exam questions should, according to Hakim, all be possible if you understand, and can apply, the material from the slides.  

## Stuff to learn
- Questions about hash functions https://docs.google.com/document/d/1h0smqF73pIhojK5yZfDlCBaLRjCUtEBUE4V3-mYJmS8/edit
- Materials for this week https://github.com/hansfranke1985/ADS/tree/master/week_2/Book
### extra stuff to learn
- Lineair algebra https://www.khanacademy.org/math/linear-algebra
- Kaggle https://www.kaggle.com/
- SQL http://sqlzoo.com/

## Extra stuff

### Communication
The Master communication is in Teams, in a team called Applied Data Science master's programme
The Data Wrangling comms is in Teams, in INFOMDWR_2020
The informal communication is in Whatsapp, in a group ADS
There's also a slack which is kinda slow atm

### Calc your grade

```python
def grading(grade_1, grade_2): if grade_1 < 5.5:
W = max(grade_1, grade_2) if W <= 5.5:
            return W
        else:
return 0.5 * (W - 6) + 6 elif grade_2 <= 5.5:
        return (grade_1 - 6) / 2 + 6
    else:
return (grade_1 - 6) / 2 + 6 + 1/5 * grade_2
```

### Want to use SQL on the CSV files?
Don't screw around with getting them into Postgres. Just use:

```python 
import pandas as pd
from pandasql import sqldf
bbc = pd.read_csv('/your/path/to/the/file/bbc.csv')
eteam = pd.read_csv('/your/path/to/the/file/eteam.csv', encoding='latin-1')
pysqldf = lambda q: sqldf(q, globals()) pysqldf('SELECT * FROM bbc LIMIT 10;')
```

### я служу советскому союзу
gen.lib.rus.ec All books
b-ok.org Better looking site, less kniga
sci-hub.tw Paywall removal

### Practice
If you wanna read that book about R i would just use this link https://r4ds.had.co.nz/  
https://course18.fast.ai/ml.html and https://mlcourse.ai/lectures are some good resources for machine learning Intro to machine learning 15 hours

# Remarks
Edited by Jelle Teijema