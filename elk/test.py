
import HtmlTestRunner
import unittest


class MyTests(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(2+2, 4)

    def test_case_2(self):
        self.assertTrue(1+1 == 2)

if __name__ == '__main__':
    # Define the test suite
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MyTests))

    # Define the output file name
    report_file = open('test_report.html', 'w')

    # Define the HTMLTestRunner object
    runner = HtmlTestRunner.HTMLTestRunner(
        stream=report_file 
    )

    # Run the test suite and generate the HTML report
    runner.run(suite)

    # Close the report file
    report_file.close()

