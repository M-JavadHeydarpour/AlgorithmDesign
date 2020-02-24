class Stable:
    def __init__(self):
        self.men = {"Xavier": ["Amy", "Bertha", "Clare", -1],
                    "Yancey": ["Bertha", "Amy", "Clare", -1],
                    "Zeus": ["Amy", "Bertha", "Clare", -1]
                    }
        self.women = {"Amy": ["Yancey", "Xavier", "Zeus", -1],
                      "Bertha": ["Xavier", "Yancey", "Zeus", -1],
                      # "Bertha": ["Zeus", "Yancey", "Xavier", -1],
                      "Clare": ["Xavier", "Yancey", "Zeus", -1]
                      }
        self.remaining_items = ["Xavier", "Yancey", "Zeus"]

    def checkMatching(self):

        while self.remaining_items:

            women = self.men[self.remaining_items[0]]  # women's list of ً man priority . man selected from
            # "remaining_items[0]" .
            woman = women[abs(women[-1]) - 1]  # first woman on man's list to whom man has not yet proposed.

            # woman is unmatched
            if self.women[woman][-1] == -1:

                # set woman's preference and man's preference.
                self.women[woman][-1] = self.women[woman].index(self.remaining_items[0])

                self.men[self.remaining_items[0]][-1] = self.men[self.remaining_items[0]].index(woman)

                del self.remaining_items[0]     # delete current man from Queue.

            # woman prefers man to her current partner man'
            elif self.women[woman][-1] > self.women[woman].index(self.remaining_items[0]):
                # second preference than
                # first.
                index = self.women[woman][-1]
                self.men[self.women[woman][index]][-1] = -1  # the unlinked man preference must be change to -1 .
                self.remaining_items.append(self.women[woman][index])  # append unlinked man to Queue of remaining .

                self.women[woman][-1] = self.women[woman].index(self.remaining_items[0])
                # update the woman preference to new man .

                self.men[self.remaining_items[0]][-1] = self.men[self.remaining_items[0]].index(woman)  # set
                # preference for man in Queue[0]

                del self.remaining_items[0]  # now delete man from Queue .

            else:
                self.men[self.remaining_items[0]][-1] -= 1  # the woman reject this man so preparing to next woman

    def stabledItems(self):

        print("Man", "\t", "Woman")
        for man in self.men:
            print(man, "\t", self.men[man][self.men[man][-1]])


if __name__ == '__main__':
    st = Stable()
    st.checkMatching()
    st.stabledItems()
