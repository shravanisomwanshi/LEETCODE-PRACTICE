class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :type rtype: List[int]
        """
        # Gördüğümüz sayıları ve indekslerini tutmak için bir sözlük (Hash Map)
        seen = {}
        
        for index, num in enumerate(nums):
            # Hedefe ulaşmak için ihtiyacımız olan diğer sayı
            complement = target - num
            
            # Eğer bu tamamlayıcı sayı daha önce sözlüğe eklendiyse, çözümü bulduk!
            if complement in seen:
                return [seen[complement], index]
            
            # Eğer yoksa, mevcut sayıyı ve indeksini sözlüğe kaydet
            seen[num] = index
            #16.7.2026 yusuf arslantas