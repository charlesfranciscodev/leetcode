import math


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        favorite_restaurants = []
        min_index_sum = math.inf
        s1 = set(list1)
        s2 = set(list2)
        intersection = s1.intersection(s2)
        for restaurant in intersection:
            index_sum = list1.index(restaurant) + list2.index(restaurant)
            if index_sum < min_index_sum:
                min_index_sum = index_sum
                favorite_restaurants = [restaurant]
            elif index_sum == min_index_sum:
                favorite_restaurants.append(restaurant)
        return favorite_restaurants
