import unittest
from ya import YaUploader


results = ["<Response [201]>", "<Response [400]>", "<Response [401]>","<Response [403]>", "<Response [404]>", "<Response [406]>", "<Response [409]>", "<Response [429]>", "<Response [503]>", "<Response [507]>"]


class YaUploaderTestCase(unittest.TestCase):
  def setUp(self):
    self.y = YaUploader('Your YaAPI Token')
  def test_nf_201(self):
    self.assertEqual(self.y.new_folder("test_folder"),results[0])
  def test_nf_400(self):
    self.assertEqual(self.y.new_folder("test_folder"),results[1])
  def test_nf_401(self):
    self.assertEqual(self.y.new_folder("test_folder"),results[2]) 
  def test_nf_403(self):
    self.assertEqual(self.y.new_folder("test_folder"),results[3])
  def test_nf_404(self):
    self.assertEqual(self.y.new_folder("test_folder"),results[4])
  def test_nf_406(self):
    self.assertEqual(self.y.new_folder("test_folder"),results[5])
  def test_nf_409(self):
    self.assertEqual(self.y.new_folder("test_folder"),results[6])
  def test_nf_429(self):
    self.assertEqual(self.y.new_folder("test_folder"),results[7])
  def test_nf_503(self):
    self.assertEqual(self.y.new_folder("test_folder"),results[8])
  def test_nf_507(self):
    self.assertEqual(self.y.new_folder("test_folder"),results[9])


if __name__ == "__main__":
  unittest.main()