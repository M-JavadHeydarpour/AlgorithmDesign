import json


class StableListMatching:
    def __init__(self, members_count):

        self.maximumMembers = members_count
        self.data = []
        self.company = {}
        self.members = {}
        self.remaining_items = []

    def load(self, path):
        path = path + '.json'
        with open(path, 'r') as file:
            self.data = json.load(file)

    def dataPreparation(self):

        for item in self.data[0].keys():
            self.remaining_items.append(item)
            self.remaining_items.append(0)

        self.company = self.data[0]
        self.members = self.data[1]

    def rm_queue(self):
        self.remaining_items[1] += 1

        if self.remaining_items[1] == self.maximumMembers:
            del self.remaining_items[0]
            del self.remaining_items[0]

    def checkMatching(self):

        while self.remaining_items:

            # members's list of ً company priority . company selected from "remaining_items[0]" .
            members = self.company[self.remaining_items[0]]

            # number of member joind to company
            members_count = members[-1][0]

            # select current index of member to select it
            members_index = members[-1][members_count + 1]

            # Select a member and then check it out and if possible connect it to the company
            member = members[abs(members_index) - 1]

            # member is unmatched
            if self.members[member][-1] == -1:

                # set member's preference and company's preference.
                self.members[member][-1] = self.members[member].index(self.remaining_items[0])

                self.company[self.remaining_items[0]][-1][0] += 1

                item_index = self.company[self.remaining_items[0]][-1][0]
                self.company[self.remaining_items[0]][-1][item_index] = self.company[self.remaining_items[0]].index(
                    member)

                # call rm_queue function for update queue
                self.rm_queue()

            # member prefers this company to her current job'
            elif self.members[member][-1] > self.members[member].index(self.remaining_items[0]):

                # the unlinked company preference must be change to -1 and count of member must be mines one  .
                index = self.members[member][-1]
                item_index = self.company[self.members[member][index]][-1][0]
                self.company[self.members[member][index]][-1][0] -= 1
                self.company[self.members[member][index]][-1][item_index] = -1

                # append unlinked company to Queue of remaining to get a member.
                self.remaining_items.append(self.members[member][index])
                self.remaining_items.append(self.maximumMembers - 1)

                # update the member preference to new company .
                self.members[member][-1] = self.members[member].index(self.remaining_items[0])

                # update company members count to count + 1
                self.company[self.remaining_items[0]][-1][0] += 1

                # set preference for company in Queue[0]
                selected_index = self.company[self.remaining_items[0]][-1][0]
                self.company[self.remaining_items[0]][-1][selected_index] = self.company[self.remaining_items[0]].index(
                    member)

                # call rm_queue function for update queue
                self.rm_queue()

            # the member reject this company so preparing to next member for this company
            else:
                item_index = self.company[self.remaining_items[0]][-1][0]
                self.company[self.remaining_items[0]][-1][item_index + 1] -= 1

    def stabledItems(self):

        print("Company", "\t", "Members")
        for co in self.company:
            result = [co]
            for member in range(1, self.maximumMembers + 1):
                result.append(self.company[co][self.company[co][-1][member]])
            print("\t,".join(result[:]))

    def save(self, path):

        path = path + '.json'
        with open(path, 'w') as file:
            output = [self.company, self.members]
            json.dump(output, file)


if __name__ == '__main__':
    st = StableListMatching(2)
    st.load('data')
    st.dataPreparation()
    st.checkMatching()
    st.stabledItems()
    st.save('result')
