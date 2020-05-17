from source.Sort import HeapSort


class IntervalPartitioning:
    def __init__(self, lectureCount=10, lecture=None):

        # [startTime, endTime, name, status]
        self.lecture = lecture
        self.lectureCount = lectureCount
        self.lectureCountSelected = 0
        self.classCount = 0
        self.scheduleItems = list()

    def sortLecture(self):
        sortObject = HeapSort(self.lectureCount, self.lecture)
        sortedLecture = sortObject.sort()

        # sorted lecture returned with tuple in index 0
        self.lecture = sortedLecture[0]

        # get number of lecture from sort class in index 1
        self.lectureCount = sortedLecture[1]

    def schedule(self):
        self.sortLecture()

        compatibility = 0
        self.scheduleItems.append([])
        while self.lectureCountSelected < self.lectureCount:

            for index in range(self.lectureCount):

                # status == 1 means lecture not be selected.
                if self.lecture[index][3] == 1:

                    # check for  having an conflict item
                    if self.lecture[index][0] >= compatibility:
                        temp = self.lecture[index][1]
                        temp2 = compatibility
                        # append selected item to result.
                        self.scheduleItems[self.classCount].append(self.lecture[index])

                        # update compatibility for next item
                        compatibility = self.lecture[index][1]

                        # set status off two provide select after this time.
                        self.lecture[index][3] = 0

                        # while all lecture not selected while loop must be continue.
                        self.lectureCountSelected += 1

                    else:
                        continue
                else:
                    continue

            self.classCount += 1
            compatibility = 0
            self.scheduleItems.append([])

        self.scheduleItems.pop()

        return '\nscheduled items :\t\t\t\t{} \n\ncounter of class we needed :\t{}\n'.format(self.scheduleItems, self.classCount)


if __name__ == "__main__":

    # first arg = lecture count and then array for scheduling
    ip = IntervalPartitioning(3, [[8, 12, 'A', 1], [1, 5, 'B', 1], [4, 9, 'C', 1]])

    print(ip.schedule())
