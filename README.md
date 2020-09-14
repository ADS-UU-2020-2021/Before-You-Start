# Before-You-Start

## Stuff you have to do:
Follow the lectures on Monday and Tuesday Exams on Thursday and Friday
Reread the slides from the lectures and learn them Lab exercises
Play around with SQL and Python on your own, best way to learn (read the book, IMO not necessary)
Enroll in elective courses


## Elective Courses
You need to enroll into elective courses, the window is already open. These are the courses to choose from: https://www.uu.nl/masters/en/applied-data-science/courses
Pick whatevery you want, you have 4 courses and thus at least 2 domains


## Info this week
You need to look up related info in the book yourself. He was going to look which chapters are related but he'll forget to do so if we don't remind him.
The actual book:

Silberscha...
Might not work if exported to PDF
The exam questions should, according to Hakim, all be possible if you understand, and can apply, the material from the slides.

## Stuff to learn
- http://sqlzoo.com/
- Questions about hash functions https://docs.google.com/document/d/1h0smqF73pIhojK5yZfDlCBaLRjCUtEBUE4V3-mYJmS8/edit
- Materials for this week https://github.com/hansfranke1985/ADS/tree/master/week_2/Book
- Lineair algebra https://www.khanacademy.org/math/linear-algebra

## Extra stuff

Calc your grade

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

## Want to use SQL on the CSV files?
Don't screw around with getting them into Postgres. Just use:

```python 
import pandas as pd
from pandasql import sqldf
bbc = pd.read_csv('/your/path/to/the/file/bbc.csv')
eteam = pd.read_csv('/your/path/to/the/file/eteam.csv', encoding='latin-1')
pysqldf = lambda q: sqldf(q, globals()) pysqldf('SELECT * FROM bbc LIMIT 10;')
```

## Stuff from the previous overview
It's still relevant!


http://gen.lib.rus.ec/ <- illegal books
b-ok.org <- more illegal books
sci-hub.tw <- no paywall
Kaggle <- practice, if you are try to a competition you'll be faced with some next level wizardry

If you wanna read that book about R i would just use this link https://r4ds.had.co.nz/ https://course18.fast.ai/ml.html and https://mlcourse.ai/lectures are some good resources for machine learning Intro to machine learning 15 hours
