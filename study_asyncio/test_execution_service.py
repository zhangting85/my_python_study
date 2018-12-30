import asyncio
import time
import traceback
import hug

def test():
    print("before sleep 2s")
    time.sleep(2)
    print("after sleep 2s")


def test2():
    print("before sleep 10s")
    assert False, "fails test2 10s"
    print("after sleep 10s")


class TestResult():
    def __init__(self,test_name,result,fail_reason=None,trace_info=None):
        self.test_name = test_name
        self.result = result
        self.fail_reason = fail_reason
        self.trace_info = trace_info


class TestRunner():
    def run(self,test_methods,mode="c"):
        """
        to run the tests methods.
        :param test_methods: the method list which will be run
        :param mode: run the tests in following modes
            c mode is to run tests concurrently.
            n mode is just run them one by one normally
        :return:
        """
        if mode == "c":
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            test_tasks = []
            for method in test_methods:
                method = self.log_test_result(method)
                test_tasks.append(self.run_tests(method))
            loop.run_until_complete(asyncio.wait(test_tasks))
            loop.close()
        elif mode == "n":
            for method in test_methods:
                method = self.log_test_result(method)
                method()

    def log_test_result(self, func):
        def wrapper(*args, **kw):
            try:
                func(*args, **kw)
            except Exception as fail_reason:
                test_result = "Fail"
                trace_info = traceback.format_exc()
                test_result = TestResult(func.__name__, test_result, fail_reason, trace_info)
                #todo: to save test result
                raise fail_reason
            else:
                test_result = "Pass"
                test_result = TestResult(func.__name__, test_result)
                # todo: to save test result
                print("")
            return
        return wrapper

    async def run_tests(self,test):
        loop = asyncio.get_event_loop()
        await loop.run_in_executor(None, test)

@hug.get() # <-- This is the only additional line
@hug.cli()
def main():
    """run test 1 and test 2"""
    start = time.time()
    tr = TestRunner()
    tr.run([test, test2], mode="c")
    end = time.time()
    return (end - start)

if __name__ == '__main__':
    main.interface.cli()

#C:\Users\colin.zt\AppData\Local\Programs\Python\Python37\Scripts\hug.exe -f test_execution_service.py