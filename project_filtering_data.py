from data import DATA


def run():
    # all_python_devs = [worker["name"]
    #                    for worker in DATA if worker["language"] == "python"]
    all_python_devs = list(map(lambda el1: el1["name"], filter(
        lambda el2: el2["language"] == "python", DATA)))
    # print(all_python_devs)
    # all_platzi_workers = [worker["name"]
    #                       for worker in DATA if worker["organization"] == "Platzi"]
    all_platzi_workers = list(map(lambda el1: el1["name"], filter(
        lambda el2: el2["organization"] == "Platzi", DATA)))
    # print(all_platzi_workers)
    # adults = list(map(lambda worker: worker["name"], filter(
    #     lambda el: el['age'] > 18, DATA)))
    adults = [worker["name"] for worker in DATA if worker['age'] > 18]
    # print(adults)
    # old_people = list(map(lambda worker: worker | {
    #                   "old": worker["age"] > 70}, DATA))
    # old_people = [worker | {"old": worker["age"] > 70} for worker in DATA]
    # using spread operator like javascript
    old_people = [{**worker, **{"old": worker["age"] > 70}} for worker in DATA]
    for worker in old_people:
        print(worker)
    # print(all_python_devs)
    # print(all_platzi_workers)
    # print(old_people)


if __name__ == '__main__':
    run()
