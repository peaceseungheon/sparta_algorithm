def back_tracking(nums, permutation, used):
    if len(permutation) == len(nums):
        print(permutation[:])  # permutation의 복사본을 출력
        return

    for i, num in enumerate(nums):
        if not used[i]:
            permutation.append(num)
            used[i] = True

            back_tracking(nums, permutation, used)

            permutation.pop()  # 방금 추가한 요소 제거
            used[i] = False  # 사용 표시 취소


def make_permutation(nums):
    back_tracking(nums, [], [False] * len(nums))

make_permutation([1, 2, 3, 4])
