def cicle(lst):
    iterator = iter(lst)
    while True:
        try:
            if iterator is None:
                raise StopIteration
            else:
                 print(next(iterator))
        except StopIteration:
            break



spis = [1,2,3,4,5,6]

cicle(spis)