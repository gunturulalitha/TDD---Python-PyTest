import pytest
# conftest.py
import time
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    #print('passed amount:', len(terminalreporter.stats['passed']))
    #print('failed amount:', len(terminalreporter.stats['failed']))
    #print('xfailed amount:', len(terminalreporter.stats['xfailed']))
    # print('skipped amount:', len(terminalreporter.stats['skipped']))

    duration = time.time() - terminalreporter._sessionstarttime
    print('duration:', duration, 'seconds')

@pytest.fixture
def input_total():
    total = 100
    return total