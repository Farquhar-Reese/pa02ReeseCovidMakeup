# CS103a Spring 22

# PA02: tracker.py and the Transaction class

(base) nick@Nicks-MacBook-Pro pa02 %  /usr/bin/env /usr/local/bin/python3 /Users/nick/.vscode/extensions/ms-python.python-2022.2.1924087327/pythonFiles/lib/python/debugpy/laun
cher 57775 -- /Users/nick/Desktop/pa02-team5/pa02/tracker.py 

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 1
id  name       description                   
---------------------------------------------
> 5
Name the transaction: Shopping
Give a description to the transaction: Went to Target
Enter in price: 25
Enter category of: food
Enter the date of the transaction: 2022-01-25
> 5
Name the transaction: Tennis Lessons
Give a description to the transaction: Recieved a Tennis Lesson from Adam
Enter in price: 50
Enter category of: leisure
Enter the date of the transaction: 2022-02-22
> 5
Name the transaction: Amazon
Give a description to the transaction: 30
Enter in price: leisure
Traceback (most recent call last):
  File "/Users/nick/Desktop/pa02-team5/pa02/tracker.py", line 169, in <module>
    toplevel()
  File "/Users/nick/Desktop/pa02-team5/pa02/tracker.py", line 135, in toplevel
    choice = process_choice(choice)
  File "/Users/nick/Desktop/pa02-team5/pa02/tracker.py", line 86, in process_choice
    amount = float((input("Enter in price: ")))
ValueError: could not convert string to float: 'leisure'
(base) nick@Nicks-MacBook-Pro pa02 %  cd /Users/nick/Desktop/pa02-team5/pa02 ; /usr/bin/env /usr/local/bin/python3 /Users/nick/.vscode/extensions/ms-python.python-2022.2.19240
87327/pythonFiles/lib/python/debugpy/launcher 57845 -- /Users/nick/Desktop/pa02-team5/pa02/tracker.py 

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 5
Name the transaction: Tennis
Give a description to the transaction: Tennis Lessons with Adam
Enter in price: 50
Enter category of: Leisure
Enter the date of the transaction: 2022-01-25
> 5
Name the transaction: Amazon
Give a description to the transaction: Bought new hat    
Enter in price: 10
Enter category of: clothing
Enter the date of the transaction: 2021-05-23
> 5
Name the transaction: Dinner
Give a description to the transaction: Dinner with Tommy
Enter in price: 80
Enter category of: Food
Enter the date of the transaction: 2020-07-03
> 7
amount     date      
----------------------------------------
10         2021-05-23
50         2022-01-25
80         2020-07-03
> 8
amount     Month     
----------------------------------------
50         01        
10         05        
80         07        
> 9
amount     Year      
----------------------------------------
80         2020      
10         2021      
50         2022      
> 10
amount     category  
----------------------------------------
80         2020      
10         2021      
50         2022      
> %                                                                                                                                                                            
(base) nick@Nicks-MacBook-Pro pa02 %  cd /Users/nick/Desktop/pa02-team5/pa02 ; /usr/bin/env /usr/local/bin/python3 /Users/nick/.vscode/extensions/ms-python.python-2022.2.19240
87327/pythonFiles/lib/python/debugpy/launcher 57868 -- /Users/nick/Desktop/pa02-team5/pa02/tracker.py 

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 5
Name the transaction: Dinner
Give a description to the transaction: Dinner with Tommy
Enter in price: 75 
Enter category of: Food
Enter the date of the transaction: 2022-12-25
> 5
Name the transaction: Lessons
Give a description to the transaction: Tennis Lessons with Adam
Enter in price: 50
Enter category of: Leisure
Enter the date of the transaction: 2021-01-02
> 5
Name the transaction: Present
Give a description to the transaction: Present for Amanda
Enter in price: 24
Enter category of: Shopping
Enter the date of the transaction: 2020-05-04
> 5      
Name the transaction: Breakfast
Give a description to the transaction: Breakfast with Reese
Enter in price: 15
Enter category of: Food
Enter the date of the transaction: 2022-04-24
> 7
amount     date      
----------------------------------------
15         2022-04-24
24         2020-05-04
50         2021-01-02
75         2022-12-25
> 8
amount     Month     
----------------------------------------
50         01        
15         04        
24         05        
75         12        
> 9
amount     Year      
----------------------------------------
24         2020      
50         2021      
90         2022      
> 10
amount     category  
----------------------------------------
24         Shopping  
50         Leisure   
90         Food      
> 4
showing transactions


id  item #     amount     category   date       description                   
----------------------------------------
1   Dinner     75         Food       2022-12-25 Dinner with Tommy             
2   Lessons    50         Leisure    2021-01-02 Tennis Lessons with Adam      
3   Present    24         Shopping   2020-05-04 Present for Amanda            
4   Breakfast  15         Food       2022-04-24 Breakfast with Reese          
> 6
Row id to delete: 1
> 4
showing transactions


id  item #     amount     category   date       description                   
----------------------------------------
2   Lessons    50         Leisure    2021-01-02 Tennis Lessons with Adam      
3   Present    24         Shopping   2020-05-04 Present for Amanda            
4   Breakfast  15         Food       2022-04-24 Breakfast with Reese          
> 

(base) nick@Nicks-MacBook-Pro pa02 % pylint tracker.py
************* Module tracker
tracker.py:89:0: C0301: Line too long (105/100) (line-too-long)
tracker.py:43:0: C0103: Constant name "menu" doesn't conform to UPPER_CASE naming style (invalid-name)
tracker.py:62:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:60:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:60:0: R0912: Too many branches (17/12) (too-many-branches)
tracker.py:60:0: R0915: Too many statements (61/50) (too-many-statements)

-----------------------------------
Your code has been rated at 9.37/10

(base) nick@Nicks-MacBook-Pro pa02 % pylint transactions.py
************* Module transactions
transactions.py:6:0: C0301: Line too long (171/100) (line-too-long)
transactions.py:31:0: C0301: Line too long (146/100) (line-too-long)
transactions.py:60:0: C0301: Line too long (153/100) (line-too-long)
transactions.py:91:0: C0301: Line too long (101/100) (line-too-long)
transactions.py:102:0: C0301: Line too long (124/100) (line-too-long)
transactions.py:112:0: C0301: Line too long (127/100) (line-too-long)
transactions.py:122:0: C0301: Line too long (109/100) (line-too-long)
transactions.py:1:0: C0114: Missing module docstring (missing-module-docstring)

-----------------------------------
Your code has been rated at 9.13/10

(base) nick@Nicks-MacBook-Pro pa02 % pytest -v
============================================================================= test session starts =============================================================================
platform darwin -- Python 3.9.7, pytest-6.2.4, py-1.10.0, pluggy-0.13.1 -- /Users/nick/opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/nick/Desktop/pa02-team5/pa02, configfile: pytest.ini
plugins: anyio-2.2.0
collected 7 items                                                                                                                                                             

test_category.py::test_to_cat_dict PASSED                                                                                                                               [ 14%]
test_category.py::test_add PASSED                                                                                                                                       [ 28%]
test_category.py::test_delete PASSED                                                                                                                                    [ 42%]
test_category.py::test_update PASSED                                                                                                                                    [ 57%]
test_transaction.py::test_selectall ERROR                                                                                                                               [ 71%]
test_transaction.py::test_select ERROR                                                                                                                                  [ 85%]
test_transaction.py::test_summarize FAILED                                                                                                                              [100%]

=================================================================================== ERRORS ====================================================================================
______________________________________________________________________ ERROR at setup of test_selectall _______________________________________________________________________
file /Users/nick/Desktop/pa02-team5/pa02/test_transaction.py, line 30
  @pytest.mark.selectall
  def test_selectall(small_db):
file /Users/nick/Desktop/pa02-team5/pa02/test_transaction.py, line 18
  @pytest.fixture
  def small_db(empty_db):
file /Users/nick/Desktop/pa02-team5/pa02/test_transaction.py, line 12
  @pytest.fixture
  def empty_db(dbile):
E       fixture 'dbile' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, dbfile, doctest_namespace, empty_db, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, small_db, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/nick/Desktop/pa02-team5/pa02/test_transaction.py:12
________________________________________________________________________ ERROR at setup of test_select ________________________________________________________________________
file /Users/nick/Desktop/pa02-team5/pa02/test_transaction.py, line 43
  @pytest.mark.select
  def test_select(small_db):
file /Users/nick/Desktop/pa02-team5/pa02/test_transaction.py, line 18
  @pytest.fixture
  def small_db(empty_db):
file /Users/nick/Desktop/pa02-team5/pa02/test_transaction.py, line 12
  @pytest.fixture
  def empty_db(dbile):
E       fixture 'dbile' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, dbfile, doctest_namespace, empty_db, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, small_db, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/nick/Desktop/pa02-team5/pa02/test_transaction.py:12
================================================================================== FAILURES ===================================================================================
_______________________________________________________________________________ test_summarize ________________________________________________________________________________

    @pytest.mark.summarize
    def test_summarize():
        ''' create new db, add rows, then summarize'''
        # add rows amount, category, date (yyyymmdd), description
>       result = Transaction(small_db).summarize()

test_transaction.py:61: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <transactions.Transaction object at 0x7fdb6f109dc0>, db_name = <function small_db at 0x7fdb6f116a60>

    def __init__(self, db_name):
        self.db_name = db_name
    
>       con = sqlite3.connect(db_name)
E       TypeError: expected str, bytes or os.PathLike object, not function

transactions.py:28: TypeError
=========================================================================== short test summary info ===========================================================================
FAILED test_transaction.py::test_summarize - TypeError: expected str, bytes or os.PathLike object, not function
ERROR test_transaction.py::test_selectall
ERROR test_transaction.py::test_select
==================================================================== 1 failed, 4 passed, 2 errors in 0.34s ====================================================================






