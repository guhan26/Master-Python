from pytest import fixture  # This line imports the fixture decorator from the pytest module
from pytest import mark  # This line imports the mark decorator from the pytest module

# simple test case
def test_firsttestcase():
    assert 1+2 == 3
    
# # Markers in pytest

# Multiple test
@mark.smoke # customised marker
def test_firsttestcase():
    assert 1+2 == 3

def test_one():
    assert 4 == 4

def test_case():
    assert 3 == 3

# flag is a global variable
flag = 1

# The testcase that is expected to fail
@mark.xfail
def testAddItemtoCart():
    assert [1,2,3] == [1,2,]
    print("add item one successful")
    global flag
    flag = 1

# Skipping a specific test function using  conditions
@mark.skipif(flag=1)
def testRemoveItemFromCart():
    print("remove item successful")

def testAddItemtoCartone():
        print("add item one successful")

# Skipping a specific test function
@mark.skip
def testRemoveItemFromCarttwo():
        print("remove item two successful")


# Test Function with Multiple Markers
@mark.smoke  # This decorator tags the test function with the smoke marker
@mark.product  # This decorator tags the test function with the product marker
def test_method_method():
    assert 6 == 3*2

@mark.product
def test_method_tw0():
    assert 5+2 == 7

@mark.product
def test_method_tree():
    assert 1+2 == 7


# # Grouping tests into classes
@mark.product  # This decorator tags the test class with the product marker
class TestProduct:

    @mark.smoke  # This decorator tags the test function with the smoke marker
    def test_method_method(self):
        assert 6 == 3*2

    def test_method_tw0(self):
        assert 5+2 == 7

    def test_method_tree(self):
        assert 1+2 == 7


# # fixtures in pytest

# fixtures will run before & after each testcases
@pytest.fixture(scope="module")
def setup():
    print("launch browser")
    print("login")
    print("browse products")

    # yield keyword execute after the fixture code is executed
    yield
    print("logoff")
    print("close browser")

def testAddItemtoCart(setup):
    print("add item one successful")

def testRemoveItemFromCart(setup):
    print("remove item successful")

def testAddItemtoCartone(setup):
    print("add item one successful")

def testRemoveItemFromCarttwo(setup):
    print("remove item two successful")


# # parametrize in pytest

# parametrize using Markers
@mark.param_testcase
@mark.parametrize("number",[1,0,100,-4])
def test_first(number):
    assert number > 0

@mark.param_testcase
@mark.parametrize("product_name,product_color",[("car","red"),("mobile","golden"),("laptop","silver")])
def test_product_detail(product_name,product_color):
    print(f" I am {product_name} with {product_color} color")
    
# parametrize using fixture
@fixture() # decorator
def fruit():
    return "apple"

@mark.fixture_sampl1
def test_fruit(fruit):
    print(f"I am {fruit}")

@fixture(params=["apple","guava","orange"])
def fruit(request):
    # Provides information on the executing test function
    return request.param  # request.param returns the current value from the params list

@mark.fixture_sampl1
def test_fruit(fruit):
    print(f"I am {fruit}")

