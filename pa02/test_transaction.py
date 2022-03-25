'''
test_categories runs unit and integration tests on the category module
'''

import pytest
from category import Category, to_cat_dict

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Category(dbfile)
    yield db

# by amanda
@pytest.mark.selectall
def test_selectall(med_db):
    ''' add a category to db, updates it, and then select all'''
    cat0 = {'name':'testing_add',
            'desc':'see if it works',
            }
    cats0 = med_db.select_all()
    assert len(cats0) == len(med_db)+1
    
 # by amanda    
@pytest.mark.select
def test_select(med_db):
    ''' add a category to db, updates it, and then select it'''
    cat0 = {'name':'testing_add',
            'desc':'see if it works',
            }
    rowid = med_db.add(cat0)
    cat1 = med_db.select_one(rowid)
    assert cat0['name']==cat1['name']
    assert cat0['desc']==cat1['desc']
    
@pytest.mark.summarize
def test_summarize():
    ''' create new db, add rows, then summarize'''
    
    # create an empty db
    df = empty_db():
    
    # add rows
    amount, category, date (yyyymmdd), description
    row1 = {'amount':35,'category':'groceries', 'date': 2022-05-02 , 'description': 'buying stuff'}
    row2 = {'amount':25,'category':'movies', 'date': 2022-05-02 , 'description': 'buying stuff'}
    row3 = {'amount':20,'category':'groceries', 'date': 2022-03-02 , 'description': 'buying stuff'}
    db.add(row1)
    db.add(row2)
    db.add(row3)
    
    result = db.summarize()
    
    assert len(result) = 2
    
    
    
    