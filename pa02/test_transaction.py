''' test_categories runs unit and integration tests on the category module'''
import pytest
from transactions import Transaction

small_db = None

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system'''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbile):
    ''' create an empty database'''
    db = Transaction(dbfile)
    yield db

@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    row1 = {'amount':35,'category':'groceries', 'date': '2022-05-02' , 'description': 'buying stuff'}
    row2 = {'amount':25,'category':'movies', 'date': '2022-05-02' , 'description': 'buying stuff'}
    row3 = {'amount':20,'category':'groceries', 'date': '2022-03-02' , 'description': 'buying stuff'}
    id1=empty_db.add(row1)
    id2=empty_db.add(row2)
    id3=empty_db.add(row3)
    small_db = empty_db

# by amanda
@pytest.mark.selectall
def test_selectall(small_db):
    ''' add a transaction to db, updates it, and then select all'''
    trans0 = {'item':'testing_add',
            'amount': 0,
            'category' : 'testing',
            'date': '2022-03-25',
            'description':'see if it works',
            }
    trans0 = small_db.select_all()
    assert len(trans0) == len(small_db)+1
    
# by amanda    
@pytest.mark.select
def test_select(small_db):
    ''' add a category to db, updates it, and then select it'''
    trans0 = {'item':'testing_add',
            'amount': 0,
            'category' : 'testing',
            'date': '2022-03-25',
            'description':'see if it works',
            }
    rowid = small_db.add(trans0)
    trans1 = small_db.select_one(rowid)
    assert trans0['itemNum']==trans1['itemNum']
    assert trans0['description']==trans1['description']

# by Reese    
@pytest.mark.update
def test_update(med_db):
    ''' this test adds a transaction to the db. Then we update it. Then we have to check to make sure we actually updated correctly.  '''
    trans0 = {'item':'testing_update',
            'amount': 69,
            'category' : 'I am testing over here...',
            'date': '2022-01-12',
            'description':'The fate of the project depends on whether this dang thing works...',
            }
    rowid = med_db.add(trans0)

    tran1 = {'item':'Lamp','amount': 44,'category':'fake food','date':'2022-04-28','description':'Please do not eat lamps. You could die...'}
    med_db.update(rowid,tran1)

    tran2 = med_db.select_one(rowid)
    assert tran2['item']==tran1['Lamp']
    assert tran2['amount']==tran1[44]
    assert tran2['category']==tran1['fake food']
    assert tran2['date']==tran1['2022-04-28']
    assert tran2['description']==tran1['Please do not eat lamps. You could die...']
    
@pytest.mark.summarize
def test_summarize():
    ''' create new db, add rows, then summarize'''
    # add rows amount, transaction, date (yyyymmdd), description
    result = Transaction(small_db).summarize()
    
    assert len(result) == 2
    
    
    
    
