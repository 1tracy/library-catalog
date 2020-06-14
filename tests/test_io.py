"""
Tests I/O Disk Operations.
"""
import retrieval

def test_check_site_state():
    """check site status"""
    assert retrieval.test_connection()

def test_get_names():
    """get the correct title"""
    test_id = 'Hc3itAEACAAJ'
    assert retrieval.id_retrieve(test_id)['volumeInfo']['title'] == 'See What Flowers'
