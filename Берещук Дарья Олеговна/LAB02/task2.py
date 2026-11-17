
STANDARD_DELIMITER = ","

def partition(arr):
    l=0
    r=len(arr)-1
    p= arr[r]
    i=l-1
    j=l
    while j<r:
        if arr[j] <= p:
            i=i+1
            arr[i], arr[j]=arr[j],arr[i]
            j=j+1
        else:
            j=j+1
    arr[r],arr[i+1]=arr[i+1],arr[r]
    return i+1


def QuickSort(arr):
    if len(arr) <= 1:
        return arr

    m = partition(arr)
    left = arr[:m]
    right = arr[m + 1:]

    return QuickSort(left) + [arr[m]] + QuickSort(right)

if __name__ == "__main__":
    numbs = input(f"Введите числа для сортировки через {STANDARD_DELIMITER}\n").split(STANDARD_DELIMITER)
    while True:
        scenario_selection = input("Сортировка по возрастанию или по убыванию?\n")
        if scenario_selection.lower() in ("по возрастанию", "повозрастанию", "возрастанию", "возрастание"):
            print(f"Ваши числа, отсортированные по возрастанию:\n{QuickSort(numbs)}")
            break
        elif scenario_selection.lower() in ("по убыванию", "поубыванию", "убыванию", "убывание"):
            print(f"Ваши числа, отсортированные по убыванию:\n{QuickSort(numbs, reverse = True)}")
            break
        else:
            print("Это плохой ответ на мой вопрос, попробуйте еще раз")




