import unittest
import Compare


class Test_Compare(unittest.TestCase):

    def test_compare_files_Return_OneError(self):
        filemaster = r"C:\Users\user\source\repos\P_CompareFiles\Source\B12345614_wzor.SPF"
        file = r"C:\Users\user\source\repos\P_CompareFiles\Source\B12345614.SPF"
        result = Compare.compare_files(filemaster, file)
        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()
