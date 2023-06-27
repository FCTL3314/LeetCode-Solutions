# Problem: 4. Median of Two Sorted Arrays


def find_median_sorted_arrays(nums1, nums2):
    common_nums = sorted(nums1 + nums2)
    len_nums = len(common_nums)
    mid = len_nums // 2
    return (common_nums[mid - 1] + common_nums[mid]) / 2 if len_nums % 2 == 0 else common_nums[mid]


answer = find_median_sorted_arrays(nums1=[1, 2], nums2=[3, 4])
print(answer)

"""
В строке №5 мы складываем списки nums1 и nums2 и сортируем их. Затем получив среднее значение длинны массива,проверяем 
чётно ли это значение, если это так то складываем два средних элемента массива и делим их на 2, иначеполучаем возвращаем 
средний элемент.
"""
