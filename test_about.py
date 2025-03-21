from store import Store
from about import About


def test_about():
    Store.verify_page()
    Store.open_about()
    About.verify_page()
    num_stats = About.get_stats()
    assert num_stats[0] > num_stats[1]
    About.go_to_main()



