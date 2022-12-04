# TASK_1
def reverse(text: str) -> str:
    if len(text) <= 1:
        return text
    else:
        return text[-1] + reverse(text[:-1])


print(reverse('hello'))


# TASK_2 sort merge
def merge_list(left_list: list, right_list: list) -> list:
    index_left = 0
    index_right = 0
    l = []
    while index_left != len(left_list) or index_right != len(right_list):
        if left_list[index_left] < right_list[index_right]:
            l.append(left_list[index_left])
            if index_left != len(left_list) - 1:
                index_left = index_left + 1
            else:
                l.extend(right_list[index_right:])
                return l
        else:
            l.append(right_list[index_right])
            if index_right != len(right_list) - 1:
                index_right = index_right + 1
            else:
                l.extend(left_list[index_left:])
                return l


def sort_list(l: list):
    if len(l) <= 2:
        return l
    else:
        mid = len(l) // 2
        left_list = l[:mid]
        right_list = l[mid:]
        if len(left_list) == 2:
            if left_list[0] > left_list[1]:
                left_list[0], left_list[1] = left_list[1], left_list[0]

        if len(right_list) == 2:
            if right_list[0] > right_list[1]:
                right_list[0], right_list[1] = right_list[1], right_list[0]

        return merge_list(sort_list(left_list), sort_list(right_list))


l1 = [1, 2, 3, 5, 2, 3, 8, 7, 10, 11, 12, 13, 18]
l2 = [6, 5, 4, 3, 2, 1]
l3 = []
print(sort_list(l1))
print(sort_list(l2))
print(sort_list(l3))
