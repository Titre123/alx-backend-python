def canUnlockAll(boxes):
    keys = []
    keys.extend(boxes[0])
    unlocked = []
    for key in keys:
        keys = list(filter((key).__ne__, keys))
        for box_i in range(1, len(boxes)):
            if key == box_i:
                unlocked.append(True)
                keys.extend(boxes[box_i])
                print(keys)

boxes = [[1], [2], [3], [4], []]
canUnlockAll(boxes)
