import unittest
#assignment assigned in CS2050 by Dr.Beaty
def findandreplace(find, replace, string):
   if string:
       if find == None or find == "":
           return string
       if replace == None:
           return string
       elif string[:len(find)] == find:
            return replace + findandreplace(find, replace, string[len(find):])
       else:
           return string[0] + findandreplace(find, replace, string[1:])
   else:
       return string



class TestFindAndReplace(unittest.TestCase):
   def test_all_none(self):
       self.assertEqual(findandreplace(None, None, None), None)

   def test_find_none(self):
       self.assertEqual(findandreplace(None, "a", "aabb"), "aabb")

   def test_find_empty(self):
       self.assertEqual(findandreplace("", "a", "aabb"), "aabb")

   def test_replace_none(self):
       self.assertEqual(findandreplace("a", None, "aabb"), "aabb")

   def test_string_none(self):
       self.assertEqual(findandreplace("a", "b", None), None)

   def test_simple(self):
       self.assertEqual(findandreplace("a", "b", "aabb"), "bbbb")

   def test_remove(self):
       self.assertEqual(findandreplace(" ", "", " a abb"), "aabb")

   def test_gettysburg(self):
       self.assertEqual(findandreplace("Four score", "Twenty", "Four score and seven years ago"), "Twenty and seven years ago")

   '''def test_list(self):
       self.assertEqual(findandreplace([1], [2], [1, 2, 3]), [2, 2, 3])'''

if __name__ == '__main__':
    unittest.main()
