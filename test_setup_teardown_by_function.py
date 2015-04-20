#######################################################################################
# Docs
#
# http://stackoverflow.com/questions/21463278/how-to-use-xunit-style-setup-function
# https://pytest.org/latest/xunit_setup.html#xunitsetup
# https://pytest.org/latest/fixture.html
#######################################################################################

# Run With
# py.test -s -v test_setup_teardown_by_function.py
# so captured output will be printed to stdout

def setup_function(func):
    print "\nsetup for %s" % func.func_name

def teardown_function(func):
    print "teardown for %s" % func.func_name

def test_setup_and_teardown():
    print "This is the test body"
    assert True
