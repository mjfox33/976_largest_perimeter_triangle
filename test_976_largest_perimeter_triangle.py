from code_976_largest_perimeter_triangle import Solution

def test_example_1():
    s = Solution()
    nums = [2,1,2]
    output = 5
    assert s.largestPerimeter(nums) == output

def test_example_2():
    s = Solution()
    nums = [1,1,2]
    output = 0
    assert s.largestPerimeter(nums) == output

def test_example_3():
    s = Solution()
    nums = [1,2,2,4,18,8]
    output = 5
    assert s.largestPerimeter(nums) == output

def test_example_4():
    s = Solution()
    nums = [3,6,2,3]
    output = 8
    assert s.largestPerimeter(nums) == output